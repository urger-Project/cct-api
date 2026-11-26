from datetime import date

from fastapi import APIRouter, HTTPException, Query

from cct_brasil_api.schemas import InstrumentDetail, InstrumentList, InstrumentType
from cct_brasil_api.services.repository import repository

router = APIRouter(prefix="/v1/instruments", tags=["instruments"])


@router.get("", response_model=InstrumentList)
def list_instruments(
    q: str | None = None,
    instrument_type: InstrumentType | None = None,
    state: str | None = Query(default=None, min_length=2, max_length=2),
    municipality: str | None = None,
    union: str | None = None,
    category: str | None = None,
    valid_on: date | None = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> InstrumentList:
    return repository.list(
        page=page,
        page_size=page_size,
        q=q,
        instrument_type=instrument_type,
        state=state.upper() if state else None,
        municipality=municipality,
        union=union,
        category=category,
        valid_on=valid_on,
    )


@router.get("/{registration_number}", response_model=InstrumentDetail)
def get_instrument(registration_number: str) -> InstrumentDetail:
    instrument = repository.get(registration_number)
    if instrument is None:
        raise HTTPException(status_code=404, detail="Instrumento coletivo não encontrado")
    return instrument

