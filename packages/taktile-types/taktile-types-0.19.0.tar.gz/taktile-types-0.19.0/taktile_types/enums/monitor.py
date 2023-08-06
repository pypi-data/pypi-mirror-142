"""Feature Monitoring types."""
from .common import ExtendedEnum


class MonitorType(ExtendedEnum):
    """Type of monitoring data"""

    NUMERIC = "numeric"
    CATEGORY = "category"
