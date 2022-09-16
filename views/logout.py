import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()

@router.get("/logout")
def logout(request: Request):
    return templates.TemplateResponse("logout.html", {"request": request})