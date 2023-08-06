from enum import Enum

from pydantic import BaseModel


class RtcToken(BaseModel):
    token: str
    channel_name: str
    user_account: str
    expired_timestamp: int


class Role(str, Enum):
    student = "student"
    teacher = "teacher"
