import flet as ft
from ui import theme
from ui.components import hud_indicator


def create_header(provider_name: str, model_name: str, latency_ms: int = None) -> ft.Control:
    latency_text = f"{latency_ms}ms" if latency_ms is not None else "--"
    return ft.Container(
        content=ft.Row(
            [
                ft.Text("JARVIS X", size=16, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                ft.Container(width=10),
                hud_indicator("Provider", provider_name, status="online", icon=ft.icons.CLOUD),
                hud_indicator("Model", model_name, status="online", icon=ft.icons.MEMORY),
                hud_indicator("Latency", latency_text, status="online" if latency_ms else "processing", icon=ft.icons.SPEED),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        bgcolor=theme.HEADER_BG,
        border=ft.border.only(bottom=ft.border.BorderSide(1, theme.CYAN_BORDER)),
    )
