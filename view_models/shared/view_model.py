"""Base model
    that should be included in all the pages
"""
from typing import Optional
from starlette.requests import Request

class ViewModelBase:

    def __init__(self, request: Request) -> None:
        
        self.request:Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__
    