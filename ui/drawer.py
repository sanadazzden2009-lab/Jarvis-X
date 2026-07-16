import flet as ft

from ui import theme
from ui.components import menu_item

DRAWER_ITEMS = [
    (ft.Icons.ADD, "New Chat"),
    (ft.Icons.HISTORY, "Conversation History"),
    (ft.Icons.STAR_BORDER, "Memory"),
    (ft.Icons.SETTINGS, "Settings"),
    (ft.Icons.SPEED, "Diagnostics"),
    (ft.Icons.CLOUD, "Providers"),
    (ft.Icons.FOLDER, "Downloads"),
    (ft.Icons.INFO, "About"),
]


def build_drawer():
    return ft.Container(
        content=ft.Column(
            [ft.Text("MENU", size=11, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD)]
            + [menu_item(icon, label) for icon, label in DRAWER_ITEMS],
            spacing=22,
        ),
        width=210,
        bgcolor=theme.DRAWER_BG,
        padding=20,
        visible=False,
    )
