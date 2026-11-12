import json

import main


def preparar_arquivo(tmp_path):
    arquivo = tmp_path / "dados.json"
    dados = {
        "contatos": [
            {"id": "1", "nome": "Ana Silva", "categoria_id": "c1"},
            {"id": "2", "nome": "Bruno Lima", "categoria_id": "c2"},
            {"id": "3", "nome": "Carla Souza", "categoria_id": "c1"},
            {"id": "4", "nome": "Diego Alves", "categoria_id": None},
            {"id": "5", "nome": "Eva Costa"},
            {"id": "6", "nome": "Fábio Lima", "categoria_id": "c99"},
        ],
        "categorias": [
            {"id": "c1", "nome": "Trabalho"},
            {"id": "c2", "nome": "Família"},
            {"id": "c3", "nome": "Amigos"},
        ],
    }
    arquivo.write_text(json.dumps(dados), encoding="utf-8")
    return arquivo


def test_filtrar_apenas_contatos_da_categoria(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    antes = arquivo.read_text(encoding="utf-8")
    contatos = main.filtrar_por_categoria("c1", arquivo)
    cadastrados = json.loads(antes)["contatos"]
    assert contatos == [cadastrados[0], cadastrados[2]]
    assert arquivo.read_text(encoding="utf-8") == antes


def test_filtrar_categoria_sem_contatos(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    assert main.filtrar_por_categoria("c3", arquivo) == []


def test_filtrar_categoria_inexistente(tmp_path):
    arquivo = preparar_arquivo(tmp_path)
    assert main.filtrar_por_categoria("c99", arquivo) == []
