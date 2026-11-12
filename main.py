import json
from pathlib import Path
from uuid import uuid4


def criar_contato(nome, arquivo=Path(__file__).with_name("dados.json")):
    arquivo = Path(arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))

    dados["contatos"].append({
        "id": str(uuid4()),
        "nome": nome,
        "cargo": "",
        "categoria_id": None,
        "favorito": False,
    })

    arquivo.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def deletar_contato(contato_id, arquivo=Path(__file__).with_name("dados.json")):
    arquivo = Path(arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))

    dados["contatos"] = [
        contato for contato in dados["contatos"] if contato["id"] != contato_id
    ]

    arquivo.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def buscar_contatos(nome, arquivo=Path(__file__).with_name("dados.json")):
    arquivo = Path(arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))

    contatos = sorted(dados["contatos"], key=lambda contato: contato["nome"])
    inicio = 0
    fim = len(contatos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = contatos[meio]["nome"]

        if nome_meio == nome:
            return contatos[meio]
        elif nome_meio < nome:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None


def criar_categoria(nome, arquivo=Path(__file__).with_name("dados.json")):
    arquivo = Path(arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))

    dados["categorias"].append({
        "id": str(uuid4()),
        "nome": nome,
    })

    arquivo.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )

def categorizar_contato(contato_id, categoria_id, arquivo=Path(__file__).with_name("dados.json")):
    arquivo = Path(arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    if not any(categoria["id"] == categoria_id for categoria in dados["categorias"]):
        return

    for contato in dados["contatos"]:
        if contato["id"] == contato_id:
            contato["categoria_id"] = categoria_id
            arquivo.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
            return


def filtrar_por_categoria(categoria_id, arquivo=Path(__file__).with_name("dados.json")):
    dados = json.loads(Path(arquivo).read_text(encoding="utf-8"))
    if not any(categoria["id"] == categoria_id for categoria in dados["categorias"]):
        return []

    return [
        contato for contato in dados["contatos"] if contato.get("categoria_id") == categoria_id
    ]