from fastapi import FastAPI
from .version import main
import httpx

app = FastAPI()

SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]

@app.get("/version")
async def return_version():
    result = main()
    return result


@app.get("/temperature")
async def return_temp():
    async with httpx.AsyncClient() as client:
        temperatures = []

        for ids in SENSEBOX_IDS:
            opensense = f"https://api.opensensemap.org/boxes/{ids}/sensors"
            res = await client.get(opensense)

            if res.status_code == 200:
                data = res.json()
                for sensor in data.get("sensors", []):
                    if sensor.get("title").lower() == "temperatur" or sensor.get("title").lower() == "temperature":
                        val = sensor.get("lastMeasurement", {}).get("value")
                        if val is not None:
                            temperatures.append(float(val))

        if not temperatures:
            return {"error": "No temperature measurements found"}

        avg_temp = sum(temperatures) / len(temperatures)
        return {"temperature_average": round(avg_temp, 2)}
