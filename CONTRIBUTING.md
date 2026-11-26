# Como contribuir

Obrigado por ajudar a tornar informações coletivas trabalhistas mais acessíveis.

## Antes de começar

- Não envie documentos privados, credenciais, dados pessoais ou informações obtidas
  por acesso restrito.
- Use somente fontes públicas cuja coleta e redistribuição sejam permitidas.
- Não apresente estimativas produzidas pelo projeto como aconselhamento jurídico,
  contábil ou trabalhista.
- Dados usados em testes devem ser sintéticos ou claramente licenciados para uso.

## Fluxo de desenvolvimento

1. Abra uma issue descrevendo a fonte, o problema ou a melhoria.
2. Crie uma branch curta a partir de `main`.
3. Instale o ambiente com `pip install -e ".[dev]"`.
4. Execute `python -m ruff check .` e `python -m pytest`.
5. Envie um pull request pequeno, com testes e documentação quando aplicável.

## Integrações de dados

Novos conectores devem registrar a URL oficial, o momento da coleta e o identificador
do instrumento. Também devem implementar limites de requisição, repetição segura e
tratamento explícito de indisponibilidade da fonte.

Não serão aceitos mecanismos destinados a contornar autenticação, CAPTCHA, bloqueios
de segurança ou restrições técnicas do provedor.

