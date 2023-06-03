# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes

"""Module that implements the embedding related functions."""

from typing import Any, List, Optional


class Embed:
    """Class that can be used to store information about embedded stuff."""

    def __init__(
        self: "Embed",
        title: Optional[str] = None,
        type_: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        timestamp: Optional[Any] = None,
        color: Optional[int] = None,
        footer: Optional[Any] = None,
        image: Optional[Any] = None,
        thumbnail: Optional[Any] = None,
        video: Optional[Any] = None,
        provider: Optional[Any] = None,
        author: Optional[str] = None,
        fields: Optional[List[dict]] = None,
    ):
        self.title = title
        self.type = type_
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.video = video
        self.provider = provider
        self.author = author
        self.fields = fields

    def asdict(self) -> dict:
        """Return the attributes as dict."""
        return {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "footer": self.footer,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "video": self.video,
            "provider": self.provider,
            "author": self.author,
            "fields": self.fields,
        }
