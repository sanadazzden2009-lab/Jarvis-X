import flet as ft

from ui import theme


def framed(content, border_color, bg_color, radius=14, thickness=1, width=None, glow=False):
    inner = ft.Container(
        content=content,
        bgcolor=bg_color,
        border_radius=max(radius - thickness, 0),
        padding=14,
    )
    shadow = (
        ft.BoxShadow(
            color=border_color,
            blur_radius=16,
            spread_radius=0,
            offset=ft.Offset(0, 0),
        )
        if glow
        else None
    )
    return ft.Container(
        content=inner,
        bgcolor=border_color,
        border_radius=radius,
        padding=thickness,
        width=width,
        shadow=shadow,
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
        width=260,
        glow=True,
    )
    return ft.Row(
        [bubble],
        alignment=ft.MainAxisAlignment.END if align_end else ft.MainAxisAlignment.START,
    )


def menu_item(icon, label):
    return ft.Container(
        content=ft.Row(
            [
                ft.Icon(icon, size=18, color=theme.TEXT_MUTED),
                ft.Text(label, size=13, color=theme.TEXT_PRIMARY),
            ],
            spacing=14,
        ),
        padding=6,
    )


# ===== HUD Indicator =====
def hud_indicator(label, value, status="online", icon=None):
    """Small HUD indicator with label, value, and status dot."""
    status_colors = {
        "online": theme.HUD_GREEN,
        "offline": theme.TEXT_MUTED,
        "error": theme.HUD_RED,
        "processing": theme.HUD_YELLOW,
    }
    dot = ft.Container(
        width=6,
        height=6,
        bgcolor=status_colors.get(status, theme.TEXT_MUTED),
        border_radius=3,
    )
    return ft.Row(
        [
            dot,
            ft.Text(label, size=9, color=theme.TEXT_MUTED),
            ft.Text(value, size=9, color=theme.TEXT_PRIMARY, weight=ft.FontWeight.W_500),
        ],
        spacing=6,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


# ===== Status Dot =====
def status_dot(status="online", size=8):
    """Return a status dot with color based on status."""
    colors = {
        "online": theme.HUD_GREEN,
        "offline": theme.TEXT_MUTED,
        "error": theme.HUD_RED,
        "processing": theme.HUD_YELLOW,
    }
    return ft.Container(
        width=size,
        height=size,
        bgcolor=colors.get(status, theme.TEXT_MUTED),
        border_radius=size / 2,
    )


# ===== Tech Panel =====
def tech_panel(content, glow_color=None, border_color=None):
    """Return a technical panel with subtle border and optional glow."""
    border = border_color or theme.CYAN_BORDER
    glow = glow_color or theme.GLOW_CYAN
    return ft.Container(
        content=content,
        bgcolor=theme.PANEL_BG,
        border=ft.border.all(1, border),
        border_radius=8,
        padding=12,
        shadow=ft.BoxShadow(
            color=glow,
            blur_radius=12,
            spread_radius=0,
            offset=ft.Offset(0, 0),
        ) if glow_color else None,
    )


# ===== Glow Container =====
def glow_container(content, glow_color, border_color=None, radius=12, padding=14):
    """Container with glow effect, similar to framed() but with explicit glow control."""
    border = border_color or theme.CYAN_BORDER
    return ft.Container(
        content=content,
        bgcolor=theme.PANEL_BG,
        border=ft.border.all(1, border),
        border_radius=radius,
        padding=padding,
        shadow=ft.BoxShadow(
            color=glow_color,
            blur_radius=20,
            spread_radius=0,
            offset=ft.Offset(0, 0),
        ),
    )


# ===== Technical Border Helper =====
def tech_border(color=None, width=1):
    """Return a border style for technical panels."""
    return ft.border.all(width, color or theme.CYAN_BORDER)
