# Modelo de dados

O contrato inicial separa entidades sindicais e instrumentos coletivos para permitir
normalização nacional sem apagar particularidades regionais.

## Instrumento coletivo

| Campo | Finalidade |
| --- | --- |
| `registration_number` | Identificador estável fornecido pela fonte |
| `instrument_type` | `CCT`, `ACT` ou `TERMO_ADITIVO` |
| `title` | Título legível do instrumento |
| `category` | Categoria profissional/econômica abrangida |
| `states` | UFs alcançadas |
| `municipalities` | Municípios alcançados |
| `valid_from` / `valid_until` | Intervalo de vigência |
| `unions` | Entidades laborais e patronais signatárias |
| `official_source_url` | Endereço público da fonte primária |
| `clauses` | Conteúdo estruturado, quando permitido |

## Entidade sindical

O campo `id` é interno e não substitui CNPJ ou registro sindical. `acronym` é tratado
como alias, pois a mesma sigla pode representar entidades diferentes. `side` distingue
representação laboral e patronal.

## Proveniência futura

Antes de ingestão de dados reais, o modelo deverá receber metadados de proveniência:

- fonte e URL oficial;
- data e versão da coleta;
- hash do conteúdo original;
- licença ou fundamento de reutilização;
- alertas de retificação ou substituição.

