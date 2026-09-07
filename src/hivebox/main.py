from fastapi import FastAPI
from version import main

app = FastAPI()

@app.get("/version")
def return_version():
    result = main()
    return result
