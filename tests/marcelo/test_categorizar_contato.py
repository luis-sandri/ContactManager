import json

import main


def preparar_arquivo(tmp_path, categoria_id=None):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Ana Silva", "categoria_id": categoria_id},
            {"id": "2", "nome": "Bruno Lima", "categoria_id": None},
        ],
        "categorias": [
            {"id": "c1", "nome": "Trabalho"},
            {"id": "c2", "nome": "Família"},
        ],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")
    return arquivo


def test_categorizar_um_contato_cadastrado(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    main.categorizar_contato("1", "c1", arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    assert dados["contatos"][0]["categoria_id"] == "c1"
    assert dados["contatos"][1]["categoria_id"] is None


def test_trocar_a_categoria_de_um_contato(tmp_path):
    arquivo = preparar_arquivo(tmp_path, "c1")
    main.categorizar_contato("1", "c2", arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    assert dados["contatos"][0]["categoria_id"] == "c2"


def test_manter_dados_quando_contato_nao_existe(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    antes = arquivo.read_text(encoding="utf-8")
    main.categorizar_contato("99", "c1", arquivo)
    assert arquivo.read_text(encoding="utf-8") == antes


def test_manter_dados_quando_categoria_nao_existe(tmp_path):
    arquivo = preparar_arquivo(tmp_path, "c1")
    antes = arquivo.read_text(encoding="utf-8")
    main.categorizar_contato("1", "c99", arquivo)
    assert arquivo.read_text(encoding="utf-8") == antes
