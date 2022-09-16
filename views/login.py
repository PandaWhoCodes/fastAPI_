import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()

@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})