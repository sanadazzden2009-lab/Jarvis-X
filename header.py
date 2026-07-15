import flet as ft

from ui import theme


def build_header(on_menu_click):
    status_dot = ft.Container(width=8, height=8, border_radius=4, bgcolor=theme.CYAN)

    return ft.Container(
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("JARVIS X", size=20, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                        ft.Row(
                            [status_dot, ft.Text("ONLINE", size=11, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD)],
                            spacing=6,
                        ),
                        ft.Text("Provider: \u2014   Model: \u2014   Latency: \u2014", size=10, color=theme.TEXT_MUTED),
                    ],
                    spacing=4,
                ),
                ft.IconButton(ft.Icons.MENU, icon_color=theme.TEXT_PRIMARY, on_click=on_menu_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=18,
        bgcolor=theme.BG_HEADER,
    )
