import flet as ft

from ui import theme
from ui.components import menu_item


def build_drawer():
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(height=10),
                ft.Text(
                    "MENU",
                    size=10,
                    color=theme.TEXT_MUTED,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=10),
                menu_item(ft.icons.DASHBOARD, "Overview"),
                menu_item(ft.icons.CHAT, "Chat"),
                menu_item(ft.icons.SETTINGS, "Settings"),
                menu_item(ft.icons.INFO, "About"),
            ],
            spacing=12,
        ),
        padding=20,
        width=200,
        bgcolor=theme.DRAWER_BG,
        border=ft.border.only(
            right=ft.border.BorderSide(1, theme.HAIRLINE)
        ),
    )
