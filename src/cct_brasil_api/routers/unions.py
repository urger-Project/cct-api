from fastapi import APIRouter, Query

from cct_brasil_api.schemas import Union
from cct_brasil_api.services.repository import repository

router = APIRouter(prefix="/v1/unions", tags=["unions"])


@router.get("", response_model=list[Union])
def list_unions(
    q: str | None = None,
    state: str | None = Query(default=None, min_length=2, max_length=2),
) -> list[Union]:
    return repository.list_unions(query=q, state=state.upper() if state else None)

