import flet as ft
from ui import theme


def build_drawer():
    """Build the side navigation drawer."""
    return ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Text("MENU", size=10, color=theme.TEXT_MUTED, weight=ft.FontWeight.BOLD),
                padding=ft.padding.only(left=16, top=16, bottom=8),
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.DASHBOARD,
                label="Overview",
                selected_icon=ft.icons.DASHBOARD,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.CHAT,
                label="Chat",
                selected_icon=ft.icons.CHAT,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.SETTINGS,
                label="Settings",
                selected_icon=ft.icons.SETTINGS,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.INFO,
                label="About",
                selected_icon=ft.icons.INFO,
            ),
        ],
        bgcolor=theme.PANEL_BG,
        indicator_color=theme.CYAN_BORDER,
    )
