import json

import main


def preparar_arquivo(tmp_path, contatos):
    arquivo = tmp_path / "dados.json"
    dados = {"contatos": contatos, "categorias": []}
    arquivo.write_text(json.dumps(dados), encoding="utf-8")
    return arquivo


def test_listar_contatos_em_ordem_alfabetica(tmp_path):
    arquivo = preparar_arquivo(tmp_path, [
        {"id": "1", "nome": "Bruno Lima"},
        {"id": "2", "nome": "Ana Silva"},
    ])
    contatos = main.listar_contatos(arquivo)
    assert [contato["nome"] for contato in contatos] == ["Ana Silva", "Bruno Lima"]


def test_listar_sem_contatos_cadastrados(tmp_path):
    arquivo = preparar_arquivo(tmp_path, [])
    assert main.listar_contatos(arquivo) == []
