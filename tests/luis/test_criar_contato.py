import json

import main


def test_cadastrar_um_novo_contato(tmp_path):
    arquivo = tmp_path / "dados.json"
    arquivo.write_text('{"contatos": [], "categorias": []}', encoding="utf-8")

    main.criar_contato("Ana Silva", arquivo)

    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    assert dados["contatos"][0]["nome"] == "Ana Silva"
