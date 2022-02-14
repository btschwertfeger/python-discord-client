

class Embed(object):

    def __init__(self,
        title: str=None,
        type: str=None,
        description: str=None,
        url: str=None,
        timestamp=None,
        color: int=None,
        footer=None,
        image=None,
        thumbnail=None,
        video=None,
        provider=None,
        author: str=None,
        fields: [dict]=None,
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
            'title': self.title,
            'type': self.type,
            'description': self.description,
            'url': self.url,
            'timestamp': self.timestamp,
            'color': self.color,
            'footer': self.footer,
            'image': self.image,
            'thumbnail': self.thumbnail,
            'video': self.video,
            'provider': self.provider,
            'author': self.author,
            'fields': self.fields
        }
