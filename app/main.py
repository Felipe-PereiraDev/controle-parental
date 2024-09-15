import flet as ft
from login import AppLogin


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_maximized = True
    page.bgcolor = ft.colors.LIGHT_BLUE_200
    page.add(
        AppLogin.tipo_conta(page=page)
    )


ft.app(main)
