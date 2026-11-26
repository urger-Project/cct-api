from datetime import date
from typing import Protocol
from unicodedata import combining, normalize

from cct_brasil_api.schemas import InstrumentDetail, InstrumentList, InstrumentType, Union


class InstrumentRepository(Protocol):
    def list(self, *, page: int, page_size: int, **filters: object) -> InstrumentList: ...

    def get(self, registration_number: str) -> InstrumentDetail | None: ...

    def list_unions(self, *, query: str | None, state: str | None) -> list[Union]: ...


def _searchable(value: str | None) -> str:
    if not value:
        return ""
    value = normalize("NFKD", value)
    return "".join(character for character in value if not combining(character)).casefold()


class InMemoryInstrumentRepository:
    """Reference repository used until a persistent adapter is configured."""

    def __init__(self, instruments: list[InstrumentDetail] | None = None) -> None:
        self._instruments = {
            instrument.registration_number: instrument for instrument in instruments or []
        }

    def upsert(self, instrument: InstrumentDetail) -> None:
        self._instruments[instrument.registration_number] = instrument

    def list(
        self,
        *,
        page: int,
        page_size: int,
        q: str | None = None,
        instrument_type: InstrumentType | None = None,
        state: str | None = None,
        municipality: str | None = None,
        union: str | None = None,
        category: str | None = None,
        valid_on: date | None = None,
        **filters: object,
    ) -> InstrumentList:
        matches = list(self._instruments.values())

        if q:
            needle = _searchable(q)
            matches = [item for item in matches if needle in self._document_text(item)]
        if instrument_type:
            matches = [item for item in matches if item.instrument_type == instrument_type]
        if state:
            matches = [item for item in matches if state.upper() in item.states]
        if municipality:
            needle = _searchable(municipality)
            matches = [
                item
                for item in matches
                if any(needle in _searchable(city) for city in item.municipalities)
            ]
        if union:
            needle = _searchable(union)
            matches = [
                item
                for item in matches
                if any(
                    needle in _searchable(entity.name)
                    or needle in _searchable(entity.acronym)
                    for entity in item.unions
                )
            ]
        if category:
            needle = _searchable(category)
            matches = [item for item in matches if needle in _searchable(item.category)]
        if valid_on:
            matches = [
                item
                for item in matches
                if (item.valid_from is None or item.valid_from <= valid_on)
                and (item.valid_until is None or item.valid_until >= valid_on)
            ]

        matches.sort(
            key=lambda item: (item.valid_from or date.min, item.registration_number), reverse=True
        )
        total = len(matches)
        start = (page - 1) * page_size
        return InstrumentList(
            items=matches[start : start + page_size],
            page=page,
            page_size=page_size,
            total=total,
        )

    def get(self, registration_number: str) -> InstrumentDetail | None:
        return self._instruments.get(registration_number)

    def list_unions(self, *, query: str | None, state: str | None) -> list[Union]:
        entities = {
            entity.id: entity
            for instrument in self._instruments.values()
            for entity in instrument.unions
        }
        matches = list(entities.values())
        if query:
            needle = _searchable(query)
            matches = [
                entity
                for entity in matches
                if needle in _searchable(entity.name) or needle in _searchable(entity.acronym)
            ]
        if state:
            matches = [entity for entity in matches if state.upper() in entity.states]
        return sorted(matches, key=lambda entity: _searchable(entity.name))

    @staticmethod
    def _document_text(instrument: InstrumentDetail) -> str:
        parts = [
            instrument.registration_number,
            instrument.title,
            instrument.category or "",
            *instrument.states,
            *instrument.municipalities,
            *instrument.clauses,
        ]
        parts.extend(entity.name for entity in instrument.unions)
        parts.extend(entity.acronym or "" for entity in instrument.unions)
        return _searchable(" ".join(parts))


repository: InstrumentRepository = InMemoryInstrumentRepository()

