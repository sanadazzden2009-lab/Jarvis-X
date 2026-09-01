import flet as ft
from ui import theme
from ui.components import message_bubble


def create_chat_view(page: ft.Page) -> ft.Control:
    messages = ft.Column(
        [],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    return ft.Container(
        content=messages,
        padding=16,
        expand=True,
        bgcolor=theme.BG_COLOR,
    )
