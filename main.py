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
