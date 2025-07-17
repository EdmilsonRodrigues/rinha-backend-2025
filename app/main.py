import os

from fastapi import FastAPI


INSTANCE_ID = os.getenv("INSTANCE_ID")
APP_PORT = os.getenv("APP_PORT")

app = FastAPI(title=INSTANCE_ID)

@app.get("/")
def health_check():
    return {"instance": INSTANCE_ID}

@app.post("/payments")
async def process_payment():
    ...


@app.get("/payments-summary")
async def get_payments_summary():
    ...

@app.get("/purge-payments")
async def purge_payments():
    ...
