import json

import main


def test_cadastrar_uma_nova_categoria(tmp_path):
    arquivo = tmp_path / "dados.json"
    arquivo.write_text('{"contatos": [], "categorias": []}', encoding="utf-8")

    main.criar_categoria("Trabalho", arquivo)

    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    assert dados["categorias"][0]["nome"] == "Trabalho"
    assert "id" in dados["categorias"][0]
