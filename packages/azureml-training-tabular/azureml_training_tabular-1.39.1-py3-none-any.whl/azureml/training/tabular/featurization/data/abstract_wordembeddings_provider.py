# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Base class for providing word embeddings."""
import logging
import os
import threading
from abc import ABC, abstractmethod
from typing import Any, Optional, cast

logger = logging.getLogger(__name__)


def get_unique_download_path(download_file: str) -> str:
    """
    Temporary function to make paths unique to node

    : return: String for path appended with current rank
    """

    rank = os.environ.get("AZUREML_PROCESS_NAME", "main")
    path = os.path.join(rank, download_file)
    return path


class AbstractWordEmbeddingsProvider(ABC):
    """Class for providing word embeddings."""

    def __init__(self, embeddings_name: str):
        """
        Initialize class for providing word embeddings.

        :param embeddings_name: Name of the embeddings asked for.
        """
        self._embeddings_name = embeddings_name
        self._embeddings_pickle_file = None  # type: Optional[str]
        self._download_folder_name = "data"
        self._embeddings_folder_name = "embeddings"
        self._lock = threading.Lock()  # type: threading.Lock
        self._tried_loading = False  # type: bool

    def __repr__(self):
        return "{}(embeddings_name='{}')".format(self.__class__.__name__, self._embeddings_name)

    def _initialize(self) -> None:
        """
        Initialize the model.

        :return: None
        """
        with self._lock:
            if self._tried_loading is False:
                self._tried_loading = True
                self._init_directories()
                self._load_from_disk()
            else:
                logger.info("Already tried loading embeddings but failed. Cancelling retry.")

    def _init_directories(self) -> None:
        """
        Initialize embeddings directories if they do not already exist.

        :return: None.
        """
        os.makedirs(self.embeddings_dir, exist_ok=True)

    @property
    def embeddings_dir(self) -> str:
        """
        Directory in which embeddings need to be stored for downloaded. Dynamic construction is necessary
        as the working directory may change throughout setup + featurization.

        :return: Directory to which embeddings have to be downloaded.
        """
        local_path = get_unique_download_path(self._download_folder_name)
        return os.path.join(os.getcwd(), local_path, self._embeddings_folder_name)

    @property
    def vector_size(self) -> int:
        """
        Return number of dimensions in the embedding model.

        :return: Number of dimensions in the embedding model.
        """
        return self._get_vector_size()

    @property
    def model(self) -> Optional[Any]:
        """
        Return the embeddings model.

        :return: The embeddings model.
        """
        return self._get_model()

    @property
    def is_lower(self) -> bool:
        """
        Return whether the embeddings trained only on lower cased words.

        :return: Whether the embeddings trained only on lower cased words.
        """
        return cast(bool, self._is_lower())

    @abstractmethod
    def _is_lower(self):
        raise NotImplementedError("Must be overridden by the implementation.")

    @abstractmethod
    def _get_model(self) -> Any:
        """
        Abstract method to be overridden to obtain model.

        :return: Should return the model object.
        """
        raise NotImplementedError()

    @abstractmethod
    def _get_vector_size(self) -> int:
        """Abstract method to be overridden to obtain vector size.

        :return: Should return vector size.
        """
        raise NotImplementedError()

    @abstractmethod
    def _load_from_disk(self) -> None:
        """
        Abstract method for loading an existing pickled model file.

        :return: None.
        """
        raise NotImplementedError()
