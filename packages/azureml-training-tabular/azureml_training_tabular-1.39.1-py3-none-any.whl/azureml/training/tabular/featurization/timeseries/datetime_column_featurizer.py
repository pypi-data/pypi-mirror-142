# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Class for featurizing datetime columns in timeseries datasets."""
import logging
from typing import Dict, List, Optional, cast

import pandas as pd

from ..._diagnostics.azureml_error import AzureMLError
from ..._diagnostics.contract import Contract
from ..._diagnostics.debug_logging import function_debug_log_wrapped
from ..._diagnostics.error_definitions import MissingColumnsInData, PandasDatetimeConversion
from ..._diagnostics.reference_codes import ReferenceCodes
from ..._types import CoreDataSingleColumnInputType
from ...timeseries._time_series_data_set import TimeSeriesDataSet
from .._azureml_transformer import AzureMLTransformer


class DatetimeColumnFeaturizer(AzureMLTransformer):
    """
    Transform that creates calendrical features for datetime-typed columns.
    This tranform contrasts with the TimeIndexFeaturizer which creates features for the time axis
    of a timeseries. Unlike the time axis, datetime columns/features do not necessarily have
    well defined frequencies, so the featurization does not include any pruning.
    """

    _FEATURE_SUFFIXES = [
        "Year",
        "Month",
        "Day",
        "DayOfWeek",
        "DayOfYear",
        "QuarterOfYear",
        "WeekOfMonth",
        "Hour",
        "Minute",
        "Second",
    ]  # type: List[str]

    def __init__(self, datetime_columns: Optional[List[str]] = None) -> None:
        Contract.assert_true(
            (datetime_columns is None) or (isinstance(datetime_columns, list)),
            "Expected datetime_columns input to be None or a list.",
            log_safe=True,
        )
        dt_cols = []  # type: List[str]
        if isinstance(datetime_columns, list):
            dt_cols = datetime_columns
        self.datetime_columns = dt_cols

    def _get_feature_names_one_column(self, input_column_name: str) -> List[str]:
        return ["{}_{}".format(input_column_name, feature) for feature in self._FEATURE_SUFFIXES]

    def _construct_datatime_feature(self, x: pd.Series) -> pd.DataFrame:
        """
        Construct the date time features from one column.

        :param x: The series with datetimes.
        :return: The data frame with features.
        """
        x_columns = self._get_feature_names_one_column(x.name)

        return pd.DataFrame(
            data=pd.concat(
                [
                    x.dt.year,  # Year
                    x.dt.month,  # Month
                    x.dt.day,  # Day
                    x.dt.dayofweek,  # DayOfWeek
                    x.dt.dayofyear,  # DayOfYear
                    x.dt.quarter,  # QuarterOfYear
                    (x.dt.day - 1) // 7 + 1,  # WeekOfMonth
                    x.dt.hour,  # Hour
                    x.dt.minute,  # Minute
                    x.dt.second,  # Second
                ],
                axis=1,
            ).values,
            columns=x_columns,
        )

    def _construct_features_from_time_columns(self, X: TimeSeriesDataSet) -> TimeSeriesDataSet:
        """
        Construct features from the datetime column.

        :param X: The input data set.
        :returns: The Time series data set with feature columns and with time column dropped.
        """
        if len(self.datetime_columns) == 0:
            return X
        for col in self.datetime_columns:
            try:
                col_as_dt = pd.to_datetime(X.data[col])
            except KeyError:
                raise AzureMLError.create(
                    MissingColumnsInData,
                    target="X",
                    reference_code=ReferenceCodes._TS_DATETIME_COLUMN_FEATURIZER_MISSING_COLUMN,
                    columns=col,
                    data_object_name="X",
                )
            except Exception:
                raise AzureMLError.create(
                    PandasDatetimeConversion,
                    target="X",
                    reference_code=ReferenceCodes._TS_DATETIME_COLUMN_FEATURIZER_PD_DATETIME_CONVERSION,
                    column=col,
                    column_type=X.data[col].dtype,
                )
            time_features = self._construct_datatime_feature(col_as_dt)
            for c in time_features.columns.values:
                X.data[c] = time_features[c].values
        X.data.drop(columns=self.datetime_columns, inplace=True)
        return X

    def preview_datetime_column_feature_names(self) -> Dict[str, List[str]]:
        """
        Get the time features names that would be generated for datetime columns.

        :return: dict that maps each raw datetime feature to a list of generated calendar feature names
        :rtype: dict
        """
        return {raw_name: self._get_feature_names_one_column(raw_name) for raw_name in self.datetime_columns}

    @function_debug_log_wrapped(logging.INFO)
    def fit(
        self, X: TimeSeriesDataSet, y: Optional[CoreDataSingleColumnInputType] = None
    ) -> "DatetimeColumnFeaturizer":
        """
        Fit the transform.

        Determine which features, if any, should be pruned.

        :param X: Input data
        :type X: azureml.automl.runtime._time_series_data_set.TimeSeriesDataSet

        :param y: Passed on to sklearn transformer fit

        :return: Fitted transform
        :rtype: azureml.automl.runtime.featurizer.transformer.timeseries.time_index_featurizer.TimeIndexFeaturizer
        """
        return self

    @function_debug_log_wrapped(logging.INFO)
    def transform(self, X: TimeSeriesDataSet) -> TimeSeriesDataSet:
        """
        Create calendrical for an input data set.

        :param X: Input data
        :type X: azureml.automl.runtime._time_series_data_set.TimeSeriesDataSet

        :return: Data frame with time index features
        :rtype: azureml.automl.runtime._time_series_data_set.TimeSeriesDataSet
        """
        return self._construct_features_from_time_columns(X)

    @function_debug_log_wrapped(logging.INFO)
    def fit_transform(
        self, X: TimeSeriesDataSet, y: Optional[CoreDataSingleColumnInputType] = None
    ) -> TimeSeriesDataSet:
        """
        Apply `fit` and `transform` methods in sequence.

        Determine which features, if any, should be pruned.

        :param X: Input data
        :type X: azureml.automl.runtime._time_series_data_set.TimeSeriesDataSet

        :param y: Passed on to sklearn transformer fit

        :return: Data frame with time index features
        :rtype: azureml.automl.runtime._time_series_data_set.TimeSeriesDataSet
        """
        X_trans = self.fit(X, y).transform(X)
        return cast(TimeSeriesDataSet, X_trans)
