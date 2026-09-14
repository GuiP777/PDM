import flet as ft
from formulario import formulario, adicionar_atividade, define_atualiza_tela
from funcoes import obter_saudacao
import atividades

def main(page: ft.Page):

    # Função que monta o Header
    def appBar():
        return ft.AppBar(
            title=ft.Text(
                "Meu IF",
                color=ft.Colors.WHITE
            ),
            bgcolor="#2b8e44",
            actions=[
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    icon_color=ft.Colors.WHITE,
                    tooltip="Adicionar atividade",
                    on_click=adicionar_atividade
                )
            ]
        )

    def listaAtividades():
        lista = []

        for atividade in atividades.carregar_atividades():
            item = ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.Text(atividade['titulo'], size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Data: {atividade['data']}", size=14),
                            ft.Text(f"Valor: {atividade['valor']}", size=14)
                        ]
                    )
                )
            )

            lista.append(item)

        return lista

    # Função de Boas Vindas
    def boasVindas():
        return ft.Container(
            content= ft.Text(
                f"Olá, {obter_saudacao()}",
                size=20
            ),
            alignment=ft.Alignment(0,1),
        )

    # Adiciona o título do projeto
    page.title = "Meu IF"

    # Adiciona o header do app
    page.appbar = appBar()

    # Adiciona apenas um texto na página
    conteudoTela = ft.ListView(
        expand=True
    )

    page.add(conteudoTela)

    def setConteudoTela():
        conteudoTela.controls.clear()
        conteudoTela.controls = [boasVindas()] + listaAtividades()

    setConteudoTela()

    page.add(formulario)

    define_atualiza_tela(setConteudoTela)

# Executa o app
if __name__ == "__main__":
    ft.run(main)