from fastapi import FastAPI
from .version import main
import datetime

app = FastAPI()

@app.get("/version")
async def return_version():
    result = main()
    return result


@app.get("/temperature")
async def return_temp():
    now = datetime.datetime.now()
    opensense = f"https://api.opensensemap.org/boxes?date={now}&phenomenon=temperature&format=:json"
    response = await client.get(opensense)
    return response
