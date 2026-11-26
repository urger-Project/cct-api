from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl


class InstrumentType(StrEnum):
    CCT = "CCT"
    ACT = "ACT"
    ADDENDUM = "TERMO_ADITIVO"


class Union(BaseModel):
    id: str
    name: str
    acronym: str | None = None
    cnpj: str | None = None
    side: str = Field(description="laboral ou patronal")
    states: list[str] = []


class InstrumentSummary(BaseModel):
    registration_number: str
    instrument_type: InstrumentType
    title: str
    category: str | None = None
    states: list[str] = []
    municipalities: list[str] = []
    valid_from: date | None = None
    valid_until: date | None = None
    unions: list[Union] = []
    official_source_url: HttpUrl | None = None


class InstrumentDetail(InstrumentSummary):
    clauses: list[str] = []


class InstrumentList(BaseModel):
    items: list[InstrumentSummary]
    page: int
    page_size: int
    total: int

