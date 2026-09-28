import uuid

atividades = [
    {
        'id': '1',
        'data': '2026-09-05',
        'titulo': 'Apresentação do app mobile',
        'valor': 10
    },
    {
        'id': '2',
        'data': '2026-09-06',
        'titulo': 'Prova de banco de dados',
        'valor': 4.5
    },
    {
        'id': '3',
        'data': '2026-09-05',
        'titulo': 'Trabalho de Qualidade de Software',
        'valor': 6
    }
]



def carregar_atividades():
    return atividades

def adicionar_atividade(atividade):
    atividade['id'] = str(uuid.uuid4())
    atividades.append(atividade)

def editar_atividade(id,atividade):
    for i, item in enumerate(atividades):
        if item['id'] == id:
            item["titulo"] = atividade ["titulo"]
            item["data"] = atividade ["data"]
            item["valor"] = atividade ["valor"]
        break

def remover_atividade(id):
    for i, item in enumerate(atividades):
        if item['id'] == id:
           atividades.remove(item)
        break