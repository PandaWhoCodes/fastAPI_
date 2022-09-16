import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

