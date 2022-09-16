from unicodedata import name
import uvicorn
import fastapi
from starlette.staticfiles import StaticFiles

from views import home
from views import account
from views import about
from views import login
from views import logout


app = fastapi.FastAPI()


def main():

    configurer()
    uvicorn.run(app, port=8000, host="0.0.0.0")


def router_configurer():
    app.include_router(home.router)
    app.include_router(about.router)
    app.include_router(account.router)
    app.include_router(login.router)
    app.include_router(logout.router)


def configurer():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    router_configurer()


if __name__ == "__main__":

    main()

else:  # this is for when we run the app in production using gunicorn
    configurer()
