import flet as ft
import json

def main(page: ft.Page):
    # Configurações principais da página
    page.window_width = 800
    page.window_height = 900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Barra de título da aplicação
    page.appbar = ft.AppBar(
        leading_width=30,
        title=ft.Text('FILTRO DE PRODUTOS POR GIRO'),
        center_title=True,
        bgcolor=ft.colors.ON_PRIMARY,
    )

    # Imagem de fundo
    img = ft.Image(
        src=f'./logiticx.png',
        width=400,
        height=150,
    )

    # Campos de filtro
    # Campo de seleção de empresa
    label_empresa = ft.Text("Selecione qual empresa que deseja pesquisar:")
    filtro_empresa = ft.Dropdown(
        options=[
            ft.dropdown.Option("LOJA 01"),
            ft.dropdown.Option("LOJA 02"),
            ft.dropdown.Option("LOJA 03"),
            ft.dropdown.Option("LOJA 04"),
        ],
        on_change=lambda e: update_setor(page, e.control.value)
    )

    # Campo de seleção de setor (inicialmente vazio)
    filtro_setor_empresa1 = ft.Dropdown(
        options=[],
        on_change=lambda e: enable_dias_dropdown()
    )
    label_setor = ft.Text('Selecione o setor que você deseja filtrar: ')

    # Campo de seleção de giro (inicialmente desabilitado)
    label_giro = ft.Text('Selecione o tipo de giro para filtrar:')
    filtro_giro = ft.Dropdown(
        options=[
            ft.dropdown.Option("giro_30"),
            ft.dropdown.Option("giro_60"),
            ft.dropdown.Option("giro_90")
        ],
        disabled=True
    )

    # Funções auxiliares
    # Habilita o dropdown de giro após a seleção de setor
    def enable_dias_dropdown():
        filtro_giro.disabled = not bool(filtro_setor_empresa1.value)
        filtro_giro.update()

    # Atualiza opções do setor com base na empresa selecionada
    def update_setor(page, empresa):
        filtro_setor_empresa1.options = []

        if empresa == "LOJA 01":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 01"),
                ft.dropdown.Option("Setor 02"),
                ft.dropdown.Option('Setor 03'),
                ft.dropdown.Option('Setor 04'),
                ft.dropdown.Option("Setor 05"),
            ]
        elif empresa == "LOJA 02":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('Setor 01'),
                ft.dropdown.Option("Setor 02"),
            ]
        elif empresa == "LOJA 03":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option("Setor 01"),
                ft.dropdown.Option('Setor 02'),
            ]
        elif empresa == "LOJA 04":
            filtro_setor_empresa1.options = [
                ft.dropdown.Option('Setor 01'),
                ft.dropdown.Option("Setor 02"),
            ]

        filtro_setor_empresa1.update()

    # Campo para exibir os dados filtrados
    valor_banco = ft.TextField(
        label="Valor do Banco de Dados", 
        value="",
        height=200,
        read_only=True,
        multiline=True
    )

    # Carrega e exibe os dados filtrados
    def carregar_dados(e):
        try:
            with open('db.json', 'r') as db:
                dados_do_banco = json.load(db)

            empresa_selecionada = filtro_empresa.value
            setor_selecionado = filtro_setor_empresa1.value
            tipo_giro = filtro_giro.value

            dados_filtrados = [
                item for item in dados_do_banco["Produtos dbo"]
                if item.get("empresa") == empresa_selecionada and item.get("setor") == setor_selecionado
            ]

            dados_filtrados_ordenados = sorted(dados_filtrados, key=lambda x: x.get(tipo_giro, 0), reverse=True)

            if dados_filtrados_ordenados:
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
                dados_formatados_str = json.dumps(dados_formatados, indent=4, ensure_ascii=False)
            else:
                dados_formatados_str = "Nenhum dado encontrado para os filtros selecionados."

            valor_banco.value = dados_formatados_str
            valor_banco.update()

        except Exception as ex:
            valor_banco.value = f"Erro ao carregar dados: {str(ex)}"
            valor_banco.update()

    # Botão para carregar dados
    botao_carregar = ft.ElevatedButton("Carregar Dados", on_click=carregar_dados)

    # Containers para organizar a interface
    container_empresa = ft.Container(content=ft.Column([label_empresa, filtro_empresa], spacing=10))
    container_setor = ft.Container(content=ft.Column([label_setor, filtro_setor_empresa1], spacing=10))
    container_giro = ft.Container(content=ft.Column([label_giro, filtro_giro], spacing=10))
    container_resposta = ft.Container(
        content=ft.Column([valor_banco, botao_carregar], spacing=10, alignment=ft.MainAxisAlignment.CENTER),
        margin=ft.margin.only(bottom=10),
        padding=10,
        alignment=ft.alignment.center,
    )

    # Container principal da página
    container_principal = ft.Container(
        content=ft.Column(
            [
                container_empresa,
                container_setor,
                container_giro,
                container_resposta
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
    )

    # Adiciona os elementos à página
    page.add(img, container_principal)

ft.app(target=main)
