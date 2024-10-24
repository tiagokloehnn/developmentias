import flet as ft
import json

def main(page: ft.Page):
    page.title = "Pesquisa de Giro"
    
    # Ajuste do estilo da página com fundo azul e opacidade
    page.bgcolor = ft.colors.with_opacity(0.5, ft.colors.BLUE)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

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

    # Criando label para selecionar o setor
    label_setor = ft.Text('Selecione o setor que você deseja filtrar: ')

    # Função para atualizar as opções do setor
    def update_setor(page, empresa):
        filtro_setor_empresa1.options = []  
        
        if empresa == "LOJA 01 - MATRIZ":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 05 - ESTOQUE CD"),
                ft.dropdown.Option("Setor 11 - ESTOQUE CD TINTAS"),
                ft.dropdown.Option('Setor 01 - PRINCIPAL LOJA 01'),
                ft.dropdown.Option('Setor 03 - ESTOQUE LOJA 01'),
                ft.dropdown.Option("Setor 04 - ESTOQUE TINTAS LOJA 01"),
            ]
        elif empresa == "LOJA 02 - INDAIAL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('Setor 01 - PRINCIPAL LOJA 02'),
                ft.dropdown.Option("Setor 04 - ESTOQUE TINTAS LOJA 02"),
            ]
        elif empresa == "LOJA 03 - DIESEL":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 05 - CD LOJA 03"),
                ft.dropdown.Option('Setor 01 - PRINCIPAL LOJA 03'),
            ]
        elif empresa == "LOJA 04 - BLUMENAU":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('Setor 01 - PRINCIPAL LOJA 04'),
                ft.dropdown.Option("Setor 04 - ESTOQUE TINTAS LOJA 04"),
            ]

        filtro_setor_empresa1.update()

    # Criando label para selecionar os dias
    label_dias = ft.Text('Selecione quantos dias para trás deseja filtrar o giro: ')

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

    # Novo dropdown para selecionar o tipo de giro (30, 60, 90 dias)
    label_giro = ft.Text('Selecione o tipo de giro para filtrar:')
    filtro_giro = ft.Dropdown(
        options=[
            ft.dropdown.Option("giro_30"),
            ft.dropdown.Option("giro_60"),
            ft.dropdown.Option("giro_90")
        ]
    )

    valor_banco = ft.TextField(
        label="Valor do Banco de Dados", 
        value="",
        height=200,
        read_only=True,  # Torna o campo não editável
        multiline=True
    )

    # Função para carregar os dados do arquivo JSON e filtrá-los
    # Função para carregar os dados do arquivo JSON e filtrá-los
    def carregar_dados(e):
        try:
            # Abrindo e lendo o arquivo JSON
            with open('db.json', 'r') as db:
                dados_do_banco = json.load(db)  # Carrega os dados do JSON

            # Obter os valores selecionados de empresa, setor e giro
            empresa_selecionada = filtro_empresa.value
            setor_selecionado = filtro_setor_empresa1.value
            tipo_giro = filtro_giro.value  # Pega o tipo de giro selecionado (30, 60 ou 90 dias)

            # Filtrar os dados com base na empresa, setor e giro
            dados_filtrados = [
                item for item in dados_do_banco["Produtos dbo"]
                if item.get("empresa") == empresa_selecionada and item.get("setor") == setor_selecionado
            ]

            # Ordenar os dados filtrados pelo valor do giro selecionado, do maior para o menor
            dados_filtrados_ordenados = sorted(dados_filtrados, key=lambda x: x.get(tipo_giro, 0), reverse=True)

            # Verifica se encontrou resultados
            if dados_filtrados_ordenados:
                # Criar uma lista apenas com os campos desejados
                dados_formatados = [
                    {
                        "codigo_produto": item["codigo_produto"],
                        "Marca": item["Marca"],
                        "giro_30": item.get("giro_30", 0),
                        "giro_60": item.get("giro_60", 0),
                        "giro_90": item.get("giro_90", 0),
                        "desc_local": item["desc_local"]
                    }
                    for item in dados_filtrados_ordenados
                ]
                
                # Convertendo os dados filtrados e formatados para string
                dados_formatados_str = json.dumps(dados_formatados, indent=4, ensure_ascii=False)
            else:
                dados_formatados_str = "Nenhum dado encontrado para os filtros selecionados."

            # Atualiza o campo de texto com os dados filtrados
            valor_banco.value = dados_formatados_str
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
    )

    container_setor = ft.Container(
        content=ft.Column(
            [label_setor, filtro_setor_empresa1],
            spacing=10
        ),
    )

    container_giro = ft.Container(
        content=ft.Column(
            [label_giro, filtro_giro],
            spacing=10
        ),
    )

    container_resposta = ft.Container(
        content=ft.Column(
            [valor_banco, botao_carregar],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER  # Centraliza o botão dentro do bloco de resposta
        ),
        margin=ft.margin.only(bottom=10),
        padding=10,
        alignment=ft.alignment.center  # Centraliza o contêiner no espaço horizontal
    )

    # Criando um contêiner centralizado com os componentes
    container_principal = ft.Container(
        content=ft.Column(
            [
                container_empresa,
                container_setor,
                container_giro,
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
