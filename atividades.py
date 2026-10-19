import uuid
import json
from pathlib import Path

pasta_atual = Path(__file__).parent
ARQUIVO_ATIVIDADES = pasta_atual.joinpath("atividades.json")

atividades = None

def carregar_atividades():
    global atividades

    if atividades is not None:
        return atividades

    if not ARQUIVO_ATIVIDADES.exists():
        atividades = []
        return atividades

    try:
        arquivo = ARQUIVO_ATIVIDADES.open("r", encoding="utf-8")
        atividades = json.load(arquivo)
        arquivo.close()
    except (json.JSONDecodeError, OSError):
        atividades = []

    return atividades

def persistir_atividades():
    arquivo = ARQUIVO_ATIVIDADES.open("w", encoding="utf-8")
    json.dump(atividades, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()

def adicionar_atividade(atividade):
    atividade['id'] = str(uuid.uuid4())
    atividades.append(atividade)

    persistir_atividades()

def editar_atividade(id,atividade):

    for i, item in enumerate(atividades):
        if item['id'] == id:
            item["titulo"] = atividade ["titulo"]
            item["data"] = atividade ["data"]
            item["valor"] = atividade ["valor"]
            break

    persistir_atividades()

def remover_atividade(id):
    for i, item in enumerate(atividades):
        if item['id'] == id:
            atividades.remove(item)
            break

    persistir_atividades()
