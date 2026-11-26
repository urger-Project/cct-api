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
    states: list[str] = Field(default_factory=list)


class InstrumentSummary(BaseModel):
    registration_number: str
    instrument_type: InstrumentType
    title: str
    category: str | None = None
    states: list[str] = Field(default_factory=list)
    municipalities: list[str] = Field(default_factory=list)
    valid_from: date | None = None
    valid_until: date | None = None
    unions: list[Union] = Field(default_factory=list)
    official_source_url: HttpUrl | None = None


class InstrumentDetail(InstrumentSummary):
    clauses: list[str] = Field(default_factory=list)


class InstrumentList(BaseModel):
    items: list[InstrumentSummary]
    page: int
    page_size: int
    total: int

