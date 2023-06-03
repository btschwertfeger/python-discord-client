from typing import Optional, List, Any


class Embed:
    def __init__(
        self: "Embed",
        title: Optional[str] = None,
        type: Optional[str] = None,
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
        self.type = type
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
