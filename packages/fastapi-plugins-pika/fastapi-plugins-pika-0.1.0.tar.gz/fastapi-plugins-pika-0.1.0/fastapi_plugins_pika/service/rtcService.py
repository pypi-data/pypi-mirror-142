from enum import Enum
import time
from typing import (
    List,
    Optional,
    Sequence,
    Union,
)

from fastapi import FastAPI, params

from fastapi_plugins_pika.schema.rtcSchema import RtcToken, Role
from fastapi_plugins_pika.service.rtcServiceImpl.RtcTokenBuilder import (
    Role_Publisher,
    Role_Subscriber,
    RtcTokenBuilder,
)


class RtcServiceClient(object):

    def generate_rtc_token(
        self,
        channel_name: str,
        user_account: str,
        role: Role,
        expire_time_in_seconds: Optional[int] = None,
    ) -> RtcToken:
        if expire_time_in_seconds is None:
            expire_time_in_seconds = self._default_expire_time_in_seconds
        expired_timestamp = int(time.time()) + expire_time_in_seconds
        if role == "student":
            role_type = Role_Publisher
        else:
            role_type = Role_Subscriber
        token = RtcTokenBuilder.buildTokenWithAccount(
            self._agora_app_id,
            self._agora_certificate_id,
            channel_name,
            user_account,
            role_type,
            expired_timestamp,
        )
        return RtcToken(
            token=token,
            channel_name=channel_name,
            user_account=user_account,
            expired_timestamp=expired_timestamp,
        )

    def __init__(
        self,
        app: FastAPI,
        agora_app_id: str,
        agora_certificate_id: str,
        default_expire_time_in_seconds: int = 3600,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
    ):
        self._agora_app_id = agora_app_id
        self._agora_certificate_id = agora_certificate_id
        self._default_expire_time_in_seconds = default_expire_time_in_seconds
        app.router.add_api_route(
            path="/rtc/token",
            endpoint=self.generate_rtc_token,
            response_model=RtcToken,
            status_code=None,
            tags=tags,
            dependencies=dependencies,
            summary="获取RTC的Token信息",
            description="",
            methods=["GET"],
            name="name",
        )


def register_rtc_service(
    app: FastAPI,
    agora_app_id: str,
    agora_certificate_id: str,
    default_expire_time_in_seconds: int = 3600,
    tags: Optional[List[Union[str, Enum]]] = None,
    dependencies: Optional[Sequence[params.Depends]] = None,
):
    RtcServiceClient(
        app=app,
        agora_app_id=agora_app_id,
        agora_certificate_id=agora_certificate_id,
        default_expire_time_in_seconds=default_expire_time_in_seconds,
        tags=tags,
        dependencies=dependencies
    )
