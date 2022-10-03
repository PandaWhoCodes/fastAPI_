from view_models.shared.view_model import ViewModelBase
from starlette.requests import Request
from services.posts_service import get_posts


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.count: int = 10
        self.page: int = 1
        self.posts = get_posts(self.count, self.page)

    """ 
    [
        {   "count" : 10
            "post_title": ""
            "post_picture": ""
            "post_excrept" : ""
        }
    ]
    """
