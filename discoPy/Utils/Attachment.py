

class Attachment(object):

    def __init__(self, 
        id: int, 
        filename: str=None, 
        description: str=None,
        content_type: str=None,
        size: int=None,
        url: str=None,
        proxy_url: str=None,
        height: int=None,
        width: int=None,
        ephemeral: bool=None
    ):
        self.id = id
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
        return {
            'id': self.id, 
            'filename': self.filename,
            'description': self.description,
            'content_type': self.content_type,
            'size': self.size,
            'url': self.url,
            'proxy_url': self.proxy_url,
            'height': self.height,
            'wisth': self.width,
            'ephemeral': self.ephemeral
        }
