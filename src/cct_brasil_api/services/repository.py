from typing import Protocol

from cct_brasil_api.schemas import InstrumentDetail, InstrumentList, Union


class InstrumentRepository(Protocol):
    def list(self, *, page: int, page_size: int, **filters: object) -> InstrumentList: ...

    def get(self, registration_number: str) -> InstrumentDetail | None: ...

    def list_unions(self, *, query: str | None, state: str | None) -> list[Union]: ...


class EmptyInstrumentRepository:
    """Placeholder until a persistent, source-backed repository is implemented."""

    def list(self, *, page: int, page_size: int, **filters: object) -> InstrumentList:
        return InstrumentList(items=[], page=page, page_size=page_size, total=0)

    def get(self, registration_number: str) -> InstrumentDetail | None:
        return None

    def list_unions(self, *, query: str | None, state: str | None) -> list[Union]:
        return []


repository: InstrumentRepository = EmptyInstrumentRepository()

