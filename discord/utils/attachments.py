# -*- coding: utf-8 -*-


"""Module that implements the attachment related functions."""

from typing import Optional


class Attachment:
    """Stores attachment related information"""

    def __init__(
        self: "Attachment",
        id_: int,
        filename: Optional[str] = None,
        description: Optional[str] = None,
        content_type: Optional[str] = None,
        size: Optional[int] = None,
        url: Optional[str] = None,
        proxy_url: Optional[str] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        ephemeral: Optional[bool] = None,
    ):
        self.id = id_
        self.filename = filename
        self.description = description
        self.content_type = content_type
        self.size = size
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
        self.ephemeral = ephemeral

    def asdict(self) -> dict:
        """Return the attributes as dict."""
        return {
            "id": self.id,
            "filename": self.filename,
            "description": self.description,
            "content_type": self.content_type,
            "size": self.size,
            "url": self.url,
            "proxy_url": self.proxy_url,
            "height": self.height,
            "width": self.width,
            "ephemeral": self.ephemeral,
        }
