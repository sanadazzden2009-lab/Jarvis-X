import flet as ft

import config
from ui import theme
from ui.header import build_header
from ui.drawer import build_drawer
from ui.core_section import build_core_section
from ui.chat_view import build_chat_view, add_exchange
from ui.input_bar import build_input_bar
from brain import process_message


def main(page: ft.Page):
    page.title = config.APP_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.BG_DARK
    page.padding = 0

    drawer = build_drawer()

    def toggle_drawer(e):
        drawer.visible = not drawer.visible
        page.update()

    header = build_header(on_menu_click=toggle_drawer)
    core_section = build_core_section()
    chat_view = build_chat_view()

    def send_message(e):
        if not user_input.value or not user_input.value.strip():
            return
        text = user_input.value.strip()
        reply = process_message(text)
        add_exchange(chat_view, text, reply)
        user_input.value = ""
        page.update()

    input_bar, user_input = build_input_bar(on_submit=send_message, on_send_click=send_message)

    main_column = ft.Column(
        [core_section, ft.Container(content=chat_view, expand=True), input_bar],
        expand=True,
        spacing=0,
    )
    body = ft.Row([drawer, main_column], expand=True, spacing=0)
    divider = ft.Container(height=1, bgcolor=theme.HAIRLINE)

    page.add(ft.Column([header, divider, body], expand=True, spacing=0))


ft.run(main)
