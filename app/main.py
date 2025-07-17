import asyncio
import os
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, Field


INSTANCE_ID = os.getenv("INSTANCE_ID")
APP_PORT = os.getenv("APP_PORT")

app = FastAPI(title=INSTANCE_ID)

@app.get("/")
def health_check():
    return {"instance": INSTANCE_ID}

class Payment(BaseModel):
    correlation_id: Annotated[UUID, Field(alias="correlationId")]
    amount: Decimal

class SummaryDetails(BaseModel):
    total_requests: Annotated[int, Field(alias="totalRequests")]
    total_amount: Annotated[Decimal, Field(alias="totalAmount")]

class PaymentsSummary(BaseModel):
    default: SummaryDetails
    fallback: SummaryDetails

async def get_default_summary() -> SummaryDetails:
    return SummaryDetails(**{
        "totalRequests": 43236,
        "totalAmount": 415542345.98
    })

async def get_fallback_summary() -> SummaryDetails:
    return SummaryDetails(**{
        "totalRequests": 423545,
        "totalAmount": 329347.34
    })


@app.post("/payments")
async def process_payment(payment: Payment) -> None:
    ...


@app.get("/payments-summary")
async def get_payments_summary() -> PaymentsSummary:
    default, fallback = await asyncio.gather(get_default_summary(), get_fallback_summary())
    return PaymentsSummary(default=default, fallback=fallback)

@app.get("/purge-payments")
async def purge_payments():
    ...
