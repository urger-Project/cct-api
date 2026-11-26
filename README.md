# CCT Brasil API

Esqueleto open source de uma API para organizar e consultar Convenções Coletivas
de Trabalho (CCT), Acordos Coletivos (ACT) e termos aditivos do Brasil.

O projeto foi pensado para o setor de terceirização e para entidades como SIEMACO,
SINDEEPRES e sindicatos equivalentes de todas as UFs. Nesta fase não há coleta,
espelhamento ou republicação de documentos: os endpoints retornam uma coleção vazia
e definem o contrato inicial da aplicação.

## Executar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
uvicorn cct_brasil_api.main:app --reload
```

Abra `http://localhost:8000/docs` para acessar a documentação OpenAPI.

## Endpoints iniciais

- `GET /health`
- `GET /v1/instruments`
- `GET /v1/instruments/{registration_number}`
- `GET /v1/unions`

Filtros previstos: texto, tipo do instrumento, UF, município, sindicato, categoria,
vigência e situação.

## Estrutura

```text
src/cct_brasil_api/
├── main.py
├── config.py
├── schemas.py
├── routers/
│   ├── health.py
│   ├── instruments.py
│   └── unions.py
└── services/
    └── repository.py
```

## Fontes futuras

A integração deverá usar somente fontes públicas e respeitar termos de uso, limites
de acesso e proteção de dados. A fonte oficial primária é o Sistema Mediador do
Ministério do Trabalho e Emprego. O projeto não é afiliado ao MTE nem aos sindicatos.

## Próximas etapas sugeridas

1. Persistência com PostgreSQL e migrações.
2. Importador de arquivos públicos/exportados do Sistema Mediador.
3. Cadastro de aliases para SIEMACO, SINDEEPRES e entidades regionais.
4. Normalização de municípios, categorias e CNPJs.
5. Busca textual e histórico de vigência.
6. Testes de integração e publicação de imagem Docker.

## Licença

MIT.

Contribuições são bem-vindas. Consulte [CONTRIBUTING.md](CONTRIBUTING.md), a
[política de segurança](SECURITY.md) e o [modelo de dados](docs/data-model.md).

