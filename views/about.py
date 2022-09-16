import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()

@router.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})