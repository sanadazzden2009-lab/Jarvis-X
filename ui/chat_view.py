import flet as ft

from ui import theme
from ui.components import message_bubble


def build_chat_view():
    return ft.ListView(expand=True, spacing=14, padding=16, auto_scroll=True)


def add_exchange(chat_view, user_text, jarvis_text):
    chat_view.controls.append(
        message_bubble("YOU", user_text, theme.AMBER, theme.PANEL_USER, theme.AMBER_BORDER, True)
    )
    chat_view.controls.append(
        message_bubble("JARVIS", jarvis_text, theme.CYAN, theme.PANEL_JARVIS, theme.CYAN_BORDER, False)
    )
