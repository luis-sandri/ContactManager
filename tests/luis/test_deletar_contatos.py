import json

import main


def test_excluir_um_contato_cadastrado(tmp_path):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Ana Silva"},
            {"id": "2", "nome": "Bruno Lima"},
        ],
        "categorias": [],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")

    main.deletar_contato("1", arquivo)

    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    nomes = [contato["nome"] for contato in dados["contatos"]]
    assert "Ana Silva" not in nomes
    assert "Bruno Lima" in nomes
