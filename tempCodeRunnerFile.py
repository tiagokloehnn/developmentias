import flet as ft
import json

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        leading_width=30,
        title=ft.Text('FILTRO DE PRODUTOS POR GIRO'),
        center_title=True,
        bgcolor=ft.colors.ON_PRIMARY,
    )

    img = ft.Image(
        src=f'./logiticx.png',
        width=400,
        height=150,
    )
