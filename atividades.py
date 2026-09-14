atividades = [
    {
        'data': '2026-09-05',
        'titulo': 'Apresentação do app mobile',
        'valor': 10
    },
    {
        'data': '2026-09-06',
        'titulo': 'Prova de banco de dados',
        'valor': 4.5
    },
    {
        'data': '2026-09-05',
        'titulo': 'Trabalho de Qualidade de Software',
        'valor': 6
    }
]



def carregar_atividades():
    return atividades

def adicionar_atividade(atividade):
    atividades.append(atividade)