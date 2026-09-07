from fastapi import FastAPI
from .version import main
import datetime
import httpx

app = FastAPI()

@app.get("/version")
async def return_version():
    result = main()
    return result


@app.get("/temperature")
async def return_temp():
    async with httpx.AsyncClient() as client:
        now = datetime.datetime.now()
        opensense = f"https://api.opensensemap.org/boxes?date={now}&phenomenon=temperature&format=:json"
        res = await client.get(opensense)
        if res.status_code == 200:
            return res.json()
