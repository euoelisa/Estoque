# Controle de Estoque — Usuários e Cargos

**Aluna:** Elisa Rita Thomas da Silva de Andrade  
**Turma:** **[PREENCHER — turma não informada]**

Projeto em Python para controlar produtos de um almoxarifado e definir usuários, cargos e permissões de acesso, com senhas armazenadas somente como hash.

## Estrutura

- `produtos/`: contém as classes já existentes do controle de estoque:
  - `produto.py`: classe `Produto`, com quantidade, preço, entrada, saída e situação de reposição;
  - `almoxarifado.py`: classe `Almoxarifado`, que reúne e movimenta produtos.
- `usuarios/`: contém os usuários do sistema:
  - `papeis.py`: cargos válidos e as permissões de cada cargo;
  - `usuario.py`: classe `Usuario`, com autenticação por hash, papéis e permissões.
- `testes/`: scripts de verificação do almoxarifado e dos usuários.

## Como executar os testes

No diretório raiz do projeto, execute:

```bash
python -m testes.teste_almoxarifado
python -m testes.teste_usuario
```

Os dois comandos devem ser executados a partir da raiz do projeto para que o Python encontre os pacotes `produtos` e `usuarios`.

## Observação de entrega

A turma não estava disponível no repositório nem no enunciado fornecido; preencha o campo indicado antes da submissão no AVA.
