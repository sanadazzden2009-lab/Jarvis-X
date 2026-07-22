import flet as ft

from ui import theme


def build_header(on_menu_click):
    status_dot = ft.Container(
        width=8,
        height=8,
        border_radius=4,
        bgcolor=theme.CYAN,
        shadow=ft.BoxShadow(
            color=theme.CYAN,
            blur_radius=8,
            spread_radius=1,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
    )

    menu_button = ft.Container(
        content=ft.IconButton(ft.Icons.MENU, icon_color=theme.CYAN, on_click=on_menu_click),
        bgcolor=theme.SURFACE,
        border_radius=12,
    )

    return ft.Container(
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("JARVIS X", size=21, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                        ft.Row(
                            [status_dot, ft.Text("ONLINE", size=11, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD)],
                            spacing=8,
                        ),
                        ft.Text("Provider: \u2014   Model: \u2014   Latency: \u2014", size=10, color=theme.TEXT_MUTED),
                    ],
                    spacing=6,
                ),
                menu_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=theme.BG_HEADER,
    )
