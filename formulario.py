import flet as ft
import atividades

atualiza_conteudo_tela = None

campo_titulo = ft.TextField(label="Título")
campo_data = ft.TextField(label="Data (YYYY-MM-DD)")
campo_valor = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)

def abrir_formulario():
    formulario.open = True
    formulario.page.update()


def fechar_formulario():
    formulario.open = False
    formulario.page.update()

def salvar_atividade():
    atividades.adicionar_atividade({
        'titulo': campo_titulo.value,
        'data': campo_data.value,
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
    abrir_formulario()

def define_atualiza_tela (funcao):
    global atualiza_conteudo_tela
    atualiza_conteudo_tela = funcao