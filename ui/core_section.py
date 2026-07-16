import flet as ft

from ui import theme


def build_core_section():
    core_circle = ft.Container(width=90, height=90, border_radius=45, bgcolor=theme.CYAN)

    return ft.Column(
        [
            ft.Container(height=30),
            core_circle,
            ft.Container(height=14),
            ft.Text("AWAITING YOUR COMMAND", size=12, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
