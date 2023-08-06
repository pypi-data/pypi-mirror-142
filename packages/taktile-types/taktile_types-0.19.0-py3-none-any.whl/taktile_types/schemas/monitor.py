"""Feature monitoring related datastructures"""
import typing as t

from pydantic import BaseModel

from taktile_types.enums.monitor import MonitorType


class MonitorData(BaseModel):
    """MonitorData of a tracked variable"""

    value: t.List[
        t.Any
    ]  # Specifying types here will influence pydantic's json rendering
    # https://github.com/samuelcolvin/pydantic/issues/2079
    type: MonitorType


class MonitoringPayload(BaseModel):
    """MonitoringPayload is the payload sent over the wire to ingester"""

    version: int = 1
    data: t.Dict[str, MonitorData]
    timestamp: int
    user_agent: t.Optional[str]
    endpoint: str
    git_sha: str
    git_ref: str
    repository_id: str


class MonitoringIngesterPayload(BaseModel):
    """Payload sent over the wire to SNS Queue"""

    message_length: int
    environment: t.Optional[str]
    message: MonitoringPayload
