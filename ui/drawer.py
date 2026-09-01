import flet as ft
from ui import theme
from ui.components import menu_item


def create_drawer(page: ft.Page) -> ft.Control:
    items = [
        menu_item(ft.icons.DASHBOARD, "Overview"),
        menu_item(ft.icons.CHAT, "Chat"),
        menu_item(ft.icons.SETTINGS, "Settings"),
        menu_item(ft.icons.INFO, "About"),
    ]
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("MENU", size=10, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD),
                *items,
            ],
            spacing=12,
        ),
        padding=20,
        bgcolor=theme.PANEL_BG,
        width=200,
        border=ft.border.only(right=ft.border.BorderSide(1, theme.CYAN_BORDER)),
    )
