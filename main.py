import flet as ft

import config
from ui import theme
from ui.header import build_header
from ui.chat_view import build_chat_view, add_exchange
from ui.input_bar import build_input_bar
from ui.core_section import build_core_section
from ui.drawer import build_drawer
from brain import process_message


def main(page: ft.Page):
    page.title = config.APP_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.BG_DARK
    page.padding = 0
    page.window.width = 400
    page.window.height = 800

    # ===== Build UI Components =====
    drawer = build_drawer()
    header = build_header(on_menu_click=lambda e: toggle_drawer(e))
    chat_view = build_chat_view()
    core_section = build_core_section()
    input_bar, user_input = build_input_bar(
        on_submit=lambda e: send_message(e),
        on_send_click=lambda e: send_message(e),
    )

    # ===== Main Layout =====
    main_content = ft.Column(
        [
            header,
            ft.Divider(height=0, color=theme.HAIRLINE),
            ft.Expanded(
                child=ft.Row(
                    [
                        drawer,
                        ft.Divider(width=0, color=theme.HAIRLINE),
                        ft.Expanded(
                            child=ft.Column(
                                [
                                    ft.Expanded(
                                        child=ft.Column(
                                            [
                                                ft.Container(height=20),
                                                core_section,
                                                ft.Container(height=20),
                                                ft.Expanded(
                                                    child=chat_view,
                                                ),
                                            ],
                                            scroll=ft.ScrollMode.AUTO,
                                        ),
                                    ),
                                    ft.Divider(height=0, color=theme.HAIRLINE),
                                    input_bar,
                                ],
                                spacing=0,
                            ),
                        ),
                    ],
                    spacing=0,
                )
            ),
        ],
        spacing=0,
    )

    page.add(main_content)

    # ===== Event Handlers =====
    def toggle_drawer(e):
        """Toggle drawer visibility."""
        drawer.visible = not drawer.visible
        page.update()

    def send_message(e):
        """Handle sending a message."""
        text = user_input.value.strip()
        if not text:
            return

        # Clear input
        user_input.value = ""
        page.update()

        # Process message through brain
        reply = process_message(text)

        # Add exchange to chat
        add_exchange(chat_view, text, reply)


ft.run(main)
