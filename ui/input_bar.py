import flet as ft

from ui import theme


def build_input_bar(on_submit, on_send_click):
    user_input = ft.TextField(
        hint_text="Ask Jarvis...",
        color=theme.TEXT_PRIMARY,
        border_color="transparent",
        focused_border_color="transparent",
        bgcolor="transparent",
        expand=True,
        on_submit=on_submit,
    )

    input_bar = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(ft.Icons.IMAGE, icon_color=theme.TEXT_MUTED, tooltip="Attach image"),
                ft.IconButton(ft.Icons.ATTACH_FILE, icon_color=theme.TEXT_MUTED, tooltip="Attach file"),
                ft.IconButton(ft.Icons.MIC, icon_color=theme.TEXT_MUTED, tooltip="Voice"),
                ft.IconButton(ft.Icons.CAMERA_ALT, icon_color=theme.TEXT_MUTED, tooltip="Camera"),
                user_input,
                ft.IconButton(ft.Icons.SEND, icon_color=theme.CYAN, tooltip="Send", on_click=on_send_click),
            ],
            spacing=2,
        ),
        bgcolor=theme.PANEL_INPUT,
        border_radius=16,
        padding=6,
        margin=16,
    )

    return input_bar, user_input
