# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility functions for memory related operations."""
import ctypes
import logging
import re
import subprocess
import sys
import warnings
from typing import Any, Tuple, cast

import numpy as np
import pandas as pd
import scipy
from sklearn.base import BaseEstimator
from sklearn.cluster import MiniBatchKMeans

from .._types import CoreDataInputType, CoreDataSingleColumnInputType

logger = logging.getLogger(__name__)
LOW_MEMORY_THRESHOLD = 0.5


if sys.platform == "win32":
    from ctypes import wintypes

    class _MEMORYSTATUSEX(ctypes.Structure):
        """The information about memory."""

        _fields_ = [
            ("dwLength", wintypes.ULONG),
            ("dwMemoryLoad", wintypes.ULONG),
            ("ullTotalPhys", wintypes.ULARGE_INTEGER),
            ("ullAvailPhys", wintypes.ULARGE_INTEGER),
            ("ullTotalPageFile", wintypes.ULARGE_INTEGER),
            ("ullAvailPageFile", wintypes.ULARGE_INTEGER),
            ("ullTotalVirtual", wintypes.ULARGE_INTEGER),
            ("ullAvailVirtual", wintypes.ULARGE_INTEGER),
            ("ullAvailExtendedVirtual", wintypes.ULARGE_INTEGER),
        ]

    def _get_ram_info_windows() -> _MEMORYSTATUSEX:
        """
        Retrieve amount of installed RAM in bytes.

        :returns: The amount of memory in bytes.
        """
        kernel32 = ctypes.windll.kernel32
        memory_status = _MEMORYSTATUSEX()
        memory_status.dwLength = ctypes.sizeof(_MEMORYSTATUSEX)
        kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))
        return memory_status


def get_all_ram() -> int:
    """
    Get all RAM in bytes.

    :returns: The RAM on the machine.
    """
    (is_success, total_memory, _) = _get_memory_using_psutil()
    if is_success:
        return total_memory

    # If we are here then psutil didnt work, then explore other options.
    if sys.platform == "win32":
        return cast(int, _get_ram_info_windows().ullTotalPhys)
    elif sys.platform == "linux":
        try:  # On Linux we can use sysconf mechanism.
            import os

            return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
        except Exception:
            message = "Failed to get total memory(RAM) on Linux."
            logger.warning(message)
            # This is last resort to get memory.
            memory_in_kb = int(
                subprocess.check_output(
                    "vmstat -s -S k | grep 'total memory' | grep -o '[[:digit:]]*'", shell=True
                ).strip()
            )
            return memory_in_kb * 1000
    elif sys.platform == "darwin":
        try:
            import ctypes
            import ctypes.util

            libc = ctypes.CDLL(str(ctypes.util.find_library("c")), use_errno=True)
            name = ctypes.create_string_buffer(b"hw.memsize")
            mem = ctypes.c_int64(0)
            output_size = ctypes.c_size_t(ctypes.sizeof(mem))
            libc.sysctlbyname(name, ctypes.byref(mem), ctypes.byref(output_size), None, 0)
            return mem.value
        except Exception:
            message = "Failed to get total memory(RAM) on MacOS."
            logger.warning(message)
            # Last resort to get total memory using system utilities through subprocess
            return int(subprocess.check_output(["sysctl", "-n", "hw.memsize"]).strip())
    else:
        logger.warning(
            "{}: Unsupported platform. Cannot determine the total memory on the machine.".format(sys.platform)
        )
        return 0


def get_available_physical_memory() -> int:
    """
    Get available physical memory in bytes.

    :returns: The available physical memory on the machine.
    """
    (is_success, _, available_memory) = _get_memory_using_psutil()
    if is_success:
        return available_memory

    if sys.platform == "win32":
        return cast(int, _get_ram_info_windows().ullAvailPhys)
    elif sys.platform == "linux":
        try:  # On Linux we can use sysconf mechanism.
            with open("/proc/meminfo", "r") as mem:
                free_memory = 0
                for i in mem:
                    sline = i.split()
                    if str(sline[0]) in ("MemFree:", "Buffers:", "Cached:"):
                        free_memory += int(sline[1])
                    elif str(sline[0]) == "MemAvailable:":
                        free_memory = int(sline[1])
                        break

                return free_memory * 1000
        except Exception:
            message = "Failed to get available(free) memory(RAM) on Linux."
            logger.warning(message)
            warnings.warn(message)
            # This is last resort to get available memory using system utilities through subprocess
            memory_in_kb = int(
                subprocess.check_output(
                    "vmstat -s -S k | grep 'free memory' | grep -o '[[:digit:]]*'", shell=True
                ).strip()
            )
            return memory_in_kb * 1000
    elif sys.platform == "darwin":
        # For macos we dont have simple api calls that can be used to query available memory
        # Hence for now relying on subprocess to this.
        """
        Returns output like this. Use regex to get all numbers and
        add all page counts. First value is page size.
        Available memory = page size * free page count
        Mach Virtual Memory Statistics: (page size of 4096 bytes)
        Pages free:                             1442394.
        Page size , Free page count.
        ['4096', '1442394']
        """
        output = re.findall(
            r"\d+", str(subprocess.check_output("vm_stat | grep -e 'Pages free' -e 'page size of'", shell=True))
        )
        available_memory = int(output[0]) * int(output[1])
        return available_memory
    else:
        logger.warning(
            "{}: Unsupported platform. Cannot determine the total memory on the machine.".format(sys.platform)
        )
        return 0


def get_data_memory_size(data: Any) -> int:
    """
    Return the total memory size of this object.

    This utility function currently supports approximate sizes of numpy ndarray,
    sparse matrix and pandas DataFrame.

    :param data: data object primarily for training
    :type data: numpy.ndarray or scipy.sparse.spmatrix or pandas.DataFrame
    :return: estimated memory size of the python object in bytes.
    """
    if scipy.sparse.issparse(data):
        memory = data.data.nbytes + data.indptr.nbytes + data.indices.nbytes  # type: int
    elif isinstance(data, pd.DataFrame):
        memory = data.memory_usage(index=True, deep=True).sum()
    elif isinstance(data, np.ndarray):
        if sys.getsizeof(data) > data.nbytes:
            memory = sys.getsizeof(data)
        else:
            memory = data.nbytes
    else:
        # For ndarrays and other object types, return memory size by sys.getsizeof()
        memory = sys.getsizeof(data)

    return memory


def _get_memory_using_psutil() -> Tuple[bool, int, int]:
    import psutil

    try:
        # is_success, total_memory, available_memory
        return True, cast(int, psutil.virtual_memory()[0]), cast(int, psutil.virtual_memory()[4])
    except Exception:
        message = "Failed to determine available(free) memory (RAM) using psutil module."
        logger.warning(message)
        warnings.warn(message)
        return False, 0, 0


def get_memory_footprint(transformer: BaseEstimator, X: CoreDataInputType, y: CoreDataSingleColumnInputType) -> int:
    """
    Obtain memory footprint estimate for this transformer.

    This method is only for the sklearn featurizer instance not an instance of AzureMLTransformer.

    :param transformer: Transformer to get memory footprint for.
    :param X: Input data.
    :param y: Input label.
    :return: Memory estimate for the transformer.
    """
    if isinstance(transformer, MiniBatchKMeans):
        return int(transformer.n_clusters * len(X) * get_data_memory_size(float))

    return 0


def _is_low_memory() -> bool:
    """
    Check available memory with a manually set fractional threshold of low memory.

    :return: Whether we are experiencing low memory based on the thresholds.
    """
    max_available_memory = get_all_ram()
    current_available_memory = get_available_physical_memory()
    logger.info(
        "Total ram: {} bytes, Current Available memory: {} bytes. "
        "Low memory threshold: {}".format(max_available_memory, current_available_memory, LOW_MEMORY_THRESHOLD)
    )

    return current_available_memory <= LOW_MEMORY_THRESHOLD * max_available_memory
