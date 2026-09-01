import flet as ft
from ui import theme
from ui.components import message_bubble


def build_chat_view() -> ft.Control:
    """Build the chat message area."""
    messages_column = ft.Column(
        [],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    chat_container = ft.Container(
        content=messages_column,
        padding=16,
        expand=True,
        bgcolor=theme.BG_DARK,
    )
    # Attach the messages column to the container for later access
    chat_container.messages_column = messages_column
    return chat_container


def add_exchange(chat_view, text, reply):
    """Add a user message and assistant reply to the chat view."""
    user_bubble = message_bubble(
        label="USER",
        text=text,
        accent=theme.HUD_GREEN,
        panel_color=theme.PANEL_BG,
        border_color=theme.HUD_GREEN,
        align_end=True,
    )
    assistant_bubble = message_bubble(
        label="JARVIS",
        text=reply,
        accent=theme.CYAN_BORDER,
        panel_color=theme.PANEL_BG,
        border_color=theme.CYAN_BORDER,
        align_end=False,
    )
    chat_view.messages_column.controls.append(user_bubble)
    chat_view.messages_column.controls.append(assistant_bubble)
    chat_view.update()
