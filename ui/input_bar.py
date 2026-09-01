import flet as ft
from ui import theme


def create_input_bar(page: ft.Page, on_send) -> ft.Control:
    text_field = ft.TextField(
        hint_text="Type command...",
        border_color=theme.CYAN_BORDER,
        bgcolor=theme.PANEL_BG,
        color=theme.TEXT_PRIMARY,
        expand=True,
    )

    def send_click(e):
        if text_field.value.strip():
            on_send(text_field.value)
            text_field.value = ""
            page.update()

    send_btn = ft.IconButton(
        icon=ft.icons.SEND,
        icon_color=theme.HUD_GREEN,
        on_click=send_click,
    )
    return ft.Container(
        content=ft.Row(
            [text_field, send_btn],
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
        bgcolor=theme.HEADER_BG,
        border=ft.border.only(top=ft.border.BorderSide(1, theme.CYAN_BORDER)),
    )
