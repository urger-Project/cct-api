from datetime import date

from cct_brasil_api.schemas import InstrumentDetail, InstrumentType, Union
from cct_brasil_api.services.repository import InMemoryInstrumentRepository


def sample_instrument() -> InstrumentDetail:
    return InstrumentDetail(
        registration_number="SYNTHETIC-0001",
        instrument_type=InstrumentType.CCT,
        title="Convenção coletiva de serviços terceirizados",
        category="Asseio e conservação",
        states=["SP"],
        municipalities=["São Paulo"],
        valid_from=date(2026, 1, 1),
        valid_until=date(2026, 12, 31),
        unions=[
            Union(
                id="synthetic-union",
                name="Sindicato Exemplo de Trabalhadores",
                acronym="SET",
                side="laboral",
                states=["SP"],
            )
        ],
        clauses=["Piso salarial e benefícios definidos no instrumento."],
    )


def test_filters_ignore_accents_and_case() -> None:
    repository = InMemoryInstrumentRepository([sample_instrument()])

    result = repository.list(page=1, page_size=20, q="CONSERVACAO", state="SP")

    assert result.total == 1
    assert result.items[0].registration_number == "SYNTHETIC-0001"


def test_validity_filter_excludes_expired_instrument() -> None:
    repository = InMemoryInstrumentRepository([sample_instrument()])

    result = repository.list(page=1, page_size=20, valid_on=date(2027, 1, 1))

    assert result.total == 0


def test_lists_unique_unions() -> None:
    instrument = sample_instrument()
    repository = InMemoryInstrumentRepository([instrument])
    repository.upsert(instrument.model_copy(update={"registration_number": "SYNTHETIC-0002"}))

    result = repository.list_unions(query="set", state="sp")

    assert len(result) == 1
    assert result[0].acronym == "SET"

