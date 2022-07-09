"""
Thankyou json to pydantic for this most tasty of treats
"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class VehicleListing(BaseModel):
    timeOfScrape: str = Field(default_factory=lambda x: datetime.now().isoformat())
    pageNumber: int
    spiderName: str
    manualRun: bool
    updatedAt: str
    updatedBy: str
    firstPublishedDate: str
    vehicleId: str
    modelYear: int
    vehicleYear: int
    bodyType: str
    colour: str
    doors: int
    engineCapacityCc: int
    fuelType: str
    vrm: str
    published: bool
    isReserved: bool
    make: str
    mileage: int
    price: int
    seats: int
    model: str
    stockType: str
    trim: str
    variant: str
    thumbnailUrl: str
    transmissionType: str
    milesPerGallon: int
    driveType: Optional[str]
    tags: List
    discountInPence: int
    engineSize: int
    fullRegistration: str
    isAvailable: bool
    selectedModel: str
    quoteType: str
    quoteAnnualMiles: int
    quoteBalanceInPence: int
    quoteApr: float
    quoteRegularPaymentInPence: int
    quoteTermMonths: int
    quoteDepositInPence: int
    quoteChargesInPence: int
    quoteResidualValueInPence: Optional[int]
    quoteExcessMileage: Optional[str]
