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

        filtro_setor_empresa1.update()  # Atualiza o dropdown na página

    # Criando label para aparecer o texto para selecionar os dias
    label_dias = ft.Text('Seleciona quantos dias para traz deseja filtrar o giro: ')

    # Campo de entrada para dias
    number_input = ft.TextField(
        label='Selecione os dias:',
        value='',  # Valor inicial como string
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: validate_input(e.control)  # Valida a entrada
    )

    # Função para validar a entrada no campo de texto
    def validate_input(control):
        # Tenta converter o valor para inteiro
        try:
            if control.value != "":
                int(control.value)  # Isso gerará um ValueError se não for um número
            control.error_text = ""  # Limpa a mensagem de erro se a conversão for bem-sucedida
        except ValueError:
            control.error_text = "Por favor, insira um número inteiro."  # Mensagem de erro

    
    

    #-----------------------------------------------------------------------------------------------------------


    
    valor_banco = ft.TextField(
        label="Valor do Banco de Dados", 
        value=""
    )

    # Função para simular a resposta de um banco de dados e atualizar o campo
    def carregar_dados(e):
        # Aqui você pode substituir pela chamada ao seu banco de dados
        dados_do_banco = "Resposta do Banco"
        valor_banco.value = dados_do_banco
        valor_banco.update()  # Atualiza a interface
    
    # Botão para carregar os dados do banco de dados
    botao_carregar = ft.ElevatedButton("Carregar Dados", on_click=carregar_dados)

    # Adicionando os campos à página
    page.add(
        label_empresa,
        filtro_empresa,
        label_setor,
        filtro_setor_empresa1,
        label_dias,
        number_input,
        valor_banco,
        botao_carregar
    )

# Executa a aplicação
ft.app(target=main)
