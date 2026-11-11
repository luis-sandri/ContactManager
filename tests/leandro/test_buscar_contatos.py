import json

import main


def test_buscar_contato_cadastrado(tmp_path):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Bruno Lima"},
            {"id": "2", "nome": "Ana Silva"},
            {"id": "3", "nome": "Carlos Souza"},
        ],
        "categorias": [],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")

    resultado = main.buscar_contatos("Ana Silva", arquivo)

    assert resultado is not None
    assert resultado["nome"] == "Ana Silva"


def test_buscar_contato_inexistente(tmp_path):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Ana Silva"},
            {"id": "2", "nome": "Bruno Lima"},
        ],
        "categorias": [],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")

    resultado = main.buscar_contatos("Leandro", arquivo)

    assert resultado is None
