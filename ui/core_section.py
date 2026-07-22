import flet as ft

from ui import theme


def _centered(inner):
    return ft.Column(
        [inner],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def build_core_section():
    inner_core = ft.Container(
        width=56,
        height=56,
        border_radius=28,
        bgcolor=theme.CYAN,
        shadow=ft.BoxShadow(
            color=theme.CYAN,
            blur_radius=22,
            spread_radius=2,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
    )

    ring = ft.Container(
        content=_centered(inner_core),
        width=104,
        height=104,
        border_radius=52,
        bgcolor=theme.CYAN_MID,
    )

    halo = ft.Container(
        content=_centered(ring),
        width=160,
        height=160,
        border_radius=80,
        bgcolor=theme.CYAN_DIM,
        shadow=ft.BoxShadow(
            color=theme.CYAN,
            blur_radius=46,
            spread_radius=2,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
    )

    return ft.Column(
        [
            ft.Container(height=26),
            halo,
            ft.Container(height=16),
            ft.Text("AWAITING YOUR COMMAND", size=12, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
