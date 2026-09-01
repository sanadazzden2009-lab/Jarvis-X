import flet as ft

from ui import theme
from ui.components import hud_indicator


def build_header(on_menu_click):
    """Build the top header with menu button and static HUD indicators."""
    return ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color=theme.TEXT_PRIMARY,
                    on_click=on_menu_click,
                    tooltip="Menu",
                ),
                ft.Text(
                    "JARVIS X",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=theme.TEXT_PRIMARY,
                ),
                ft.Container(width=10),
                hud_indicator(
                    "Provider",
                    "Groq",
                    status="online",
                    icon=ft.icons.CLOUD,
                ),
                hud_indicator(
                    "Model",
                    "gpt-oss-120b",
                    status="online",
                    icon=ft.icons.MEMORY,
                ),
                hud_indicator(
                    "Latency",
                    "--",
                    status="processing",
                    icon=ft.icons.SPEED,
                ),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        bgcolor=theme.BG_HEADER,
        border=ft.border.only(
            bottom=ft.border.BorderSide(1, theme.CYAN_BORDER)
        ),
    )
