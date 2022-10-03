import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from utils import get_return_template
from view_models.home.index_view_model import IndexViewModel

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()


@router.get("/")
def home(request: Request):
    vm = IndexViewModel(request=request)
    return get_return_template("index.html", request, vm.to_dict())

