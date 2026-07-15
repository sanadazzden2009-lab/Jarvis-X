import flet as ft

from ui import theme


def framed(content, border_color, bg_color, radius=14, thickness=1, width=None):
    inner = ft.Container(
        content=content,
        bgcolor=bg_color,
        border_radius=max(radius - thickness, 0),
        padding=12,
    )
    return ft.Container(
        content=inner,
        bgcolor=border_color,
        border_radius=radius,
        padding=thickness,
        width=width,
    )


def message_bubble(label, text, accent, panel_color, border_color, align_end):
    bubble = framed(
        ft.Column(
            [
                ft.Text(label, size=10, weight=ft.FontWeight.BOLD, color=accent),
                ft.Text(text, size=14, color=theme.TEXT_PRIMARY),
            ],
            spacing=6,
        ),
        border_color=border_color,
        bg_color=panel_color,
        width=250,
    )
    return ft.Row(
        [bubble],
        alignment=ft.MainAxisAlignment.END if align_end else ft.MainAxisAlignment.START,
    )


def menu_item(icon, label):
    return ft.Row(
        [
            ft.Icon(icon, size=18, color=theme.TEXT_MUTED),
            ft.Text(label, size=13, color=theme.TEXT_PRIMARY),
        ],
        spacing=12,
    )
