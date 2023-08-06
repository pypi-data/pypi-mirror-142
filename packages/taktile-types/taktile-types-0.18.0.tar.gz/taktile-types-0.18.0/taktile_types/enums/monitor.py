"""Feature Monitoring types."""
from .common import ExtendedEnum


class MonitorType(ExtendedEnum, str):
    """Type of monitoring data"""

    NUMERIC = "numeric"
    CATEGORY = "category"
