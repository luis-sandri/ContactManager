import json

import main


def preparar_arquivo(tmp_path):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Ana Silva", "favorito": False},
            {"id": "2", "nome": "Bruno Lima", "favorito": False},
        ],
        "categorias": [],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")
    return arquivo


def test_favoritar_um_contato_cadastrado(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    main.favoritar_contato("1", arquivo)
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    assert dados["contatos"][0]["favorito"] is True
    assert dados["contatos"][1]["favorito"] is False


def test_manter_dados_quando_contato_nao_existe(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    antes = arquivo.read_text(encoding="utf-8")
    main.favoritar_contato("99", arquivo)
    assert arquivo.read_text(encoding="utf-8") == antes