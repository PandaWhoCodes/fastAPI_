import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()

@router.get("/account")
def account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})
