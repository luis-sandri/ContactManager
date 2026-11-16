import json

import main


def test_editar_cargo_contato(tmp_path):
    arquivo = tmp_path / "dados.json"

    dados = {
        "contatos": [
            {
                "id": "2",
                "nome": "Bruno Lima",
                "cargo": "Analista",
                "categoria_id": None,
                "favorito": False
            }
        ],
        "categorias": []
    }

    arquivo.write_text(json.dumps(dados), encoding="utf-8")

    main.editar_cargo("2", "Gerente", arquivo)

    resultado = json.loads(arquivo.read_text(encoding="utf-8"))
    contato = resultado["contatos"][0]

    assert contato["cargo"] == "Gerente"
    assert contato["nome"] == "Bruno Lima"

