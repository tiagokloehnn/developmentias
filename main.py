import flet as ft

def main(page: ft.Page):
    page.title = "Pesquisa de Giro"

    # Criando campo para pesquisar por empresa
    label_empresa = ft.Text("Selecione qual empresa que deseja pesquisar:")
    filtro_empresa = ft.Dropdown(
        options=[
            ft.dropdown.Option("LOJA 01 - MATRIZ"),
            ft.dropdown.Option("LOJA 02 - INDAIAL"),
            ft.dropdown.Option("LOJA 03 - DIESEL"),
            ft.dropdown.Option("LOJA 04 - BLUMENAU"),
        ],
        width=200,
        on_change=lambda e: update_setor(page, e.control.value)  # Atualiza o setor ao mudar a empresa
    )

    # Campo para setor, inicialmente vazio
    filtro_setor_empresa1 = ft.Dropdown(
        options=[],
        width=500
    )

    # Criando label para aparecer o texto
    label_setor = ft.Text('Selecione o setor que você deseja filtrar: ')

    # Função para atualizar as opções do setor
    def update_setor(page, empresa):
        # Limpa as opções antes de adicionar novas
        filtro_setor_empresa1.options = []  
        
        if empresa == "LOJA 01 - MATRIZ":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 05 - CD"),
                ft.dropdown.Option("Setor 11 - CD TINTAS"),
                ft.dropdown.Option('LOJA 1 - PRINCIPAL LOJA'),
                ft.dropdown.Option('LOJA 01 - ESTOQUE 03'),
                ft.dropdown.Option("LOJA 01 - ESTOQUE TINTAS"),
            ]
        elif empresa == "LOJA 02 - INDAIAL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('LOJA 2 - PRINCIPAL LOJA'),
                ft.dropdown.Option("LOJA 01 - ESTOQUE TINTAS"),
            ]
        elif empresa == "DIESEL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("LOJA 03 - CD"),
                ft.dropdown.Option('LOJA 1 - PRINCIPAL LOJA'),
            ]
        elif empresa == "LOJA 04 - BLUMENAU":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('LOJA 1 - PRINCIPAL LOJA'),
                ft.dropdown.Option("LOJA 01 - ESTOQUE TINTAS"),
            ]

        filtro_setor_empresa1.update()  # Atualiza o dropdown na página

    # Adicionando os campos à página
    page.add(
        label_empresa,
        filtro_empresa,
        label_setor,
        filtro_setor_empresa1
    )

ft.app(target=main)
