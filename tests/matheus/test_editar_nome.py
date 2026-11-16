import json

import main


def test_editar_nome_contato(tmp_path):
    arquivo = tmp_path / "dados.json"

    dados = {
        "contatos": [
            {
                "id": "1",
                "nome": "Ana Silva",
                "cargo": "Analista",
                "categoria_id": None,
                "favorito": False
            }
        ],
        "categorias": []
    }

    arquivo.write_text(json.dumps(dados), encoding="utf-8")

    main.editar_nome("1", "Ana Oliveira", arquivo)

    resultado = json.loads(arquivo.read_text(encoding="utf-8"))
    contato = resultado["contatos"][0]

    assert contato["nome"] == "Ana Oliveira"
    assert contato["cargo"] == "Analista"
