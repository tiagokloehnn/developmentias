import flet as ft
import json

def main(page: ft.Page):
    page.title = "Pesquisa de Giro"
    
    # Ajuste do estilo da página com fundo azul e opacidade
    page.bgcolor = ft.colors.with_opacity(0.5, ft.colors.BLUE)  # Define o fundo azul com opacidade
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza os itens verticalmente
    
    # Criando campo para pesquisar por empresa
    label_empresa = ft.Text("Selecione qual empresa que deseja pesquisar:")
    filtro_empresa = ft.Dropdown(
        options=[
            ft.dropdown.Option("LOJA 01 - MATRIZ"),
            ft.dropdown.Option("LOJA 02 - INDAIAL"),
            ft.dropdown.Option("LOJA 03 - DIESEL"),
            ft.dropdown.Option("LOJA 04 - BLUMENAU"),
        ],
        on_change=lambda e: update_setor(page, e.control.value)  # Atualiza o setor ao mudar a empresa
    )

    # Campo para setor, inicialmente vazio
    filtro_setor_empresa1 = ft.Dropdown(
        options=[],
    )

    # Criando label para aparecer o texto
    label_setor = ft.Text('Selecione o setor que você deseja filtrar: ')

    # Função para atualizar as opções do setor
    def update_setor(page, empresa):
        filtro_setor_empresa1.options = []  
        
        if empresa == "LOJA 01 - MATRIZ":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 05 - CD"),
                ft.dropdown.Option("Setor 11 - CD TINTAS"),
                ft.dropdown.Option("LOJA 01 - PRINCIPAL LOJA"),
                ft.dropdown.Option("LOJA 01 - ESTOQUE 03"),
                ft.dropdown.Option("LOJA 01 - ESTOQUE TINTAS"),
            ]
        elif empresa == "LOJA 02 - INDAIAL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('LOJA 02 - PRINCIPAL LOJA'),
                ft.dropdown.Option("LOJA 02 - ESTOQUE TINTAS"),
            ]
        elif empresa == "LOJA 03 - DIESEL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("LOJA 03 - CD"),
                ft.dropdown.Option('LOJA 03 - PRINCIPAL LOJA'),
            ]
        elif empresa == "LOJA 04 - BLUMENAU":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('LOJA 04 - PRINCIPAL LOJA'),
                ft.dropdown.Option("LOJA 04 - ESTOQUE TINTAS"),
            ]

        filtro_setor_empresa1.update()

    # Criando label para aparecer o texto para selecionar os dias
    label_dias = ft.Text('Seleciona quantos dias para traz deseja filtrar o giro: ')

    # Campo de entrada para dias
    number_input = ft.TextField(
        label='Selecione os dias:',
        value='',
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: validate_input(e.control)
    )

    # Função para validar a entrada no campo de texto
    def validate_input(control):
        try:
            if control.value != "":
                int(control.value)
            control.error_text = ""
        except ValueError:
            control.error_text = "Por favor, insira um número inteiro."

    valor_banco = ft.TextField(
        label="Valor do Banco de Dados", 
        value="",
    )

    # Função para carregar os dados do arquivo JSON
    def carregar_dados(e):
        try:
            # Abrindo e lendo o arquivo JSON
            with open('db.json', 'r') as f:
                dados_do_banco = json.load(f)  # Carrega os dados do JSON

            # Convertendo os dados para string formatada
            dados_formatados = json.dumps(dados_do_banco, indent=4, ensure_ascii=False)

            # Atualiza o campo de texto com os dados do banco de dados
            valor_banco.value = dados_formatados
            valor_banco.update()

        except Exception as ex:
            valor_banco.value = f"Erro ao carregar dados: {str(ex)}"
            valor_banco.update()

    # Botão para carregar os dados do banco de dados
    botao_carregar = ft.ElevatedButton("Carregar Dados", on_click=carregar_dados)

    # Criando containers para cada bloco de seleção e resposta
    container_empresa = ft.Container(
        content=ft.Column(
            [label_empresa, filtro_empresa],
            spacing=10  # Espaçamento interno
        ),
        margin=ft.margin.only(bottom=40),  # Margem inferior
        padding=10  # Adiciona espaçamento ao redor
    )

    container_setor = ft.Container(
        content=ft.Column(
            [label_setor, filtro_setor_empresa1],
            spacing=10
        ),
        margin=ft.margin.only(bottom=40),
        padding=10
    )

    container_dias = ft.Container(
        content=ft.Column(
            [label_dias, number_input],
            spacing=10
        ),
        margin=ft.margin.only(bottom=40),
        padding=10
    )

    container_resposta = ft.Container(
        content=ft.Column(
            [valor_banco, botao_carregar],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER  # Centraliza o botão dentro do bloco de resposta
        ),
        margin=ft.margin.only(bottom=40),
        padding=10,
        alignment=ft.alignment.center  # Centraliza o contêiner no espaço horizontal
    )

    # Criando um contêiner centralizado com os componentes
    container_principal = ft.Container(
        content=ft.Column(
            [
                container_empresa,
                container_setor,
                container_dias,
                container_resposta
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente os itens
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
            spacing=20  # Define o espaçamento entre os itens (20 pixels neste exemplo)
        ),
        alignment=ft.alignment.center,  # Centraliza o contêiner na página
    )

    # Adicionando o contêiner principal à página
    page.add(container_principal)

# Executa a aplicação
ft.app(target=main)
