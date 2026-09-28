import flet as ft
import atividades

atualiza_conteudo_tela = None
atividade_em_edicao = None
atividade_para_exclusao = None

campo_titulo = ft.TextField(label="Título")
campo_data = ft.TextField(label="Data (YYYY-MM-DD)")
campo_valor = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)

def abrir_formulario():
    formulario.open = True
    formulario.page.update()

def fechar_formulario():
    formulario.open = False
    formulario.page.update()

def abrir_confirma_exclusao():
    confirma_exclusao.open = True
    confirma_exclusao.page.update()

def fechar_confirma_exclusao():
    confirma_exclusao.open = False
    confirma_exclusao.page.update()

def excluir_atividade():
    atividades.remover_atividade(atividade_para_exclusao['id'])
    atualiza_conteudo_tela()
    fechar_confirma_exclusao()

confirma_exclusao = ft.AlertDialog(
    modal=True,
    title=ft.Text("Exclusão"),
    content=ft.Text("Deseja realmente excluir a atividade?"),
    actions=[
        ft.TextButton("Cancelar", on_click=fechar_confirma_exclusao),
        ft.TextButton("Excluir", on_click=excluir_atividade)
    ],
    actions_alignment=ft.MainAxisAlignment.END
)


def salvar_atividade():
    global atividade_em_edicao

    if atividade_em_edicao is None:
        atividades.adicionar_atividade({
            'data': campo_data.value,
            'titulo': campo_titulo.value,
            'valor': campo_valor.value
        })
    else:
        atividades.editar_atividade(atividade_em_edicao['id'], {
            'data': campo_data.value,
            'titulo': campo_titulo.value,
            'valor': campo_valor.value
        })

    atualiza_conteudo_tela()
    fechar_formulario()

    campo_titulo.value = ''
    campo_data.value = ''
    campo_valor.value = ''

formulario = ft.AlertDialog(
    title=ft.Text("Nova Atividade"),
    content=ft.Column(
        controls=[
            campo_titulo,
            campo_data,
            campo_valor
        ],
        tight=True,
        spacing=10
    ),
    actions=[
        ft.TextButton("Cancelar", on_click=fechar_formulario),
        ft.TextButton("Salvar", on_click=salvar_atividade)
    ],
)

def adicionar_atividade():
    global atividade_em_edicao
    atividade_em_edicao = None
    abrir_formulario()

def editar_atividade(atividade):
    global atividade_em_edicao
    atividade_em_edicao = atividade

    campo_titulo.value = atividade["titulo"]
    campo_data.value = atividade["data"]
    campo_valor.value = atividade["valor"]

    abrir_formulario()

def define_atualiza_tela (funcao):
    global atualiza_conteudo_tela
    atualiza_conteudo_tela = funcao

def remover_atividade(atividade):
    global atividade_para_exclusao
    atividade_para_exclusao = atividade

    confirma_exclusao.content = ft.Text(
        f"Deseja realmente excluir:\n{atividade_para_exclusao['titulo']}"
    )

    abrir_confirma_exclusao()
