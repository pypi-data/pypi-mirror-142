"""Optional utilities for converting sources of data into PyTorch-compatible datasets."""
PAST_IND_KEY = 'PAST_REGRESSOR'
PAST_DEP_KEY = 'PAST_REGRESSAND'
FUTURE_IND_KEY = 'FUTURE_REGRESSOR'
FUTURE_DEP_KEY = 'FUTURE_REGRESSAND'

PAST_IND_KEY_UTF = 'PAST_UNTRANSFORMED_REGRESSOR'
PAST_DEP_KEY_UTF = 'PAST_UNTRANSFORMED_REGRESSAND'
FUTURE_IND_KEY_UTF = 'FUTURE_UNTRANSFORMED_REGRESSOR'
FUTURE_DEP_KEY_UTF = 'FUTURE_UNTRANSFORMED_REGRESSAND'

from forecast.data.dataset import TimeSeriesDataset  # noqa: F401, E402
from forecast.data.sources.data_source import AbstractDataSource, DataSourceConfig  # noqa: F401, E402
