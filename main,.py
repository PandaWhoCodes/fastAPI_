from unicodedata import name
import uvicorn
import fastapi


app =  fastapi.FastAPI()

@app.get("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app,port=8000,host="0.0.0.0")