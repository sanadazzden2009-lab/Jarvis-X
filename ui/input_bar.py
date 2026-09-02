import flet as ft

from ui import theme


def build_input_bar(on_submit, on_send_click):
    """Build the input bar and return (input_bar, user_input)."""

    user_input = ft.TextField(
        hint_text="Type command...",
        border_color=theme.CYAN_BORDER,
        bgcolor=theme.BG_INPUT,      # أصبح معرفًا في theme.py
        color=theme.TEXT_PRIMARY,
        expand=True,
        on_submit=on_submit,
    )

    send_btn = ft.IconButton(
        icon=ft.icons.SEND,
        icon_color=theme.HUD_GREEN,
        on_click=on_send_click,
    )

    input_bar = ft.Container(
        content=ft.Row(
            [
                user_input,
                send_btn,
            ],
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
        bgcolor=theme.HEADER_BG,      # تم التصحيح
        border=ft.border.only(
            top=ft.border.BorderSide(1, theme.CYAN_BORDER),
        ),
    )

    return input_bar, user_input
