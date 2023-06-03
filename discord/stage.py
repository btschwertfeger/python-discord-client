# -*- coding: utf-8 -*-


"""Module that implements the REST stagerelated functions."""


from typing import Any, Optional

from discord.base_request import BaseRequestAPI


class Stage(BaseRequestAPI):
    """Contains a collection of stage related methods."""

    def create_stage_instance(
        self, channel_id: str, topic: str, privacy_level: Optional[int] = None
    ) -> dict:
        """https://discord.com/developers/docs/resources/stage-instance#create-stage-instance"""
        payload: dict = {
            "channel_id": channel_id,
            "topic": topic,
            "privacy_level": privacy_level,
        }
        return self._request(  # type: ignore[no-any-return]
            "POST",
            params={k: v for k, v in payload.items() if v is not None},
            uri="/stage-instances",
        )

    def get_stage_instance(self, channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/stage-instance#get-stage-instance"""
        return self._request(  # type: ignore[no-any-return]
            "GET", uri=f"/stage-instances/{channel_id}"
        )

    def modify_stage_instance(
        self,
        channel_id: str,
        topic: Optional[str] = None,
        privacy_level: Optional[Any] = None,
    ) -> dict:
        """https://discord.com/developers/docs/resources/stage-instance#modify-stage-instance"""
        payload: dict = {"topic": topic, "privacy_level": privacy_level}
        return self._request(  # type: ignore[no-any-return]
            "PATCH",
            params={k: v for k, v in payload.items() if v is not None},
            uri=f"/stage-instances/{channel_id}",
        )

    def delete_stage_instance(self: "Stage", channel_id: str) -> dict:
        """https://discord.com/developers/docs/resources/stage-instance#delete-stage-instance"""
        return self._request(  # type: ignore[no-any-return]
            "DELETE", uri=f"/stage-instances/{channel_id}"
        )
