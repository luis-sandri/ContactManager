# Gerenciador de contatos

Projeto acadêmico de gerenciamento de contatos. As funções disponíveis são criar um contato, excluir um contato pelo ID, buscar um contato pelo nome e criar uma categoria. Os dados ficam salvos em `dados.json`, sem campo de telefone.

## Preparar o ambiente

No terminal, entre na pasta do projeto e execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

No Windows, use `python -m venv .venv` para criar o ambiente e `.venv\Scripts\Activate.ps1` para ativá-lo no PowerShell.

## Usar pelo terminal

Na raiz do projeto, com o ambiente virtual ativo, abra o Python com as funções carregadas:

```bash
python -i main.py
```

Os próximos comandos são digitados no console do Python (`>>>`). Executar apenas `python main.py` não abre um menu.

### Criar contatos

```python
criar_contato("Ana Silva")
criar_contato("Bruno Lima")
```

Cada contato recebe um ID automático, nome, cargo vazio, `categoria_id` sem associação e `favorito` falso. Os contatos existentes são preservados. Não há validação de nomes duplicados.

### Buscar um contato pelo nome

```python
buscar_contatos("Ana Silva")
```

A função ordena os contatos pelo nome e realiza uma busca binária, retornando o dicionário do contato encontrado ou `None` caso o nome não esteja cadastrado.

### Criar categorias

```python
criar_categoria("Trabalho")
```

Cada categoria criada recebe um ID automático e o nome informado, sendo adicionada à lista `"categorias"` em `dados.json`.

### Consultar o arquivo e encontrar o ID

```python
print(Path("dados.json").read_text(encoding="utf-8"))
```

Esse comando mostra o arquivo JSON para você copiar o campo `id` do contato que deseja excluir.

### Excluir um contato

Substitua o texto abaixo pelo ID de Ana, mantendo as aspas:

```python
deletar_contato("cole-o-id-da-ana-aqui")
```

Confira novamente o arquivo para verificar que Ana foi removida e Bruno permanece:

```python
print(Path("dados.json").read_text(encoding="utf-8"))
```

Um ID inexistente não remove nenhum contato. Esses comandos alteram o `dados.json` real do projeto.

### Sair

```python
exit()
```

## Arquivo de dados

O `dados.json` já acompanha o projeto com a estrutura inicial:

```json
{
  "contatos": [],
  "categorias": []
}
```

O arquivo precisa existir e conter um JSON válido. As categorias criadas são salvas em `"categorias"`, e `categoria_id` nos contatos está reservado para associar um contato ao ID de uma categoria.

## Executar os testes

No terminal, fora do console Python e na raiz do projeto:

```bash
python -m pytest tests/luis/test_criar_contato.py -v
python -m pytest tests/luis/test_deletar_contatos.py -v
python -m pytest tests/leandro/test_buscar_contatos.py -v
python -m pytest tests/leandro/test_criar_categorias.py -v
```

Para executar todos os testes:

```bash
python -m pytest
```

Os testes usam arquivos JSON temporários e não alteram o `dados.json` do projeto. Os testes das demais funcionalidades ficam nas pastas dos respectivos responsáveis; alguns ainda estão marcados como pendentes (`skipped`).
