import flet as ft

import config
from ui import theme
import ui.components


def main(page: ft.Page):
    page.title = config.APP_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.BG_DARK
    page.padding = 0

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Text(
                "STEP 3",
                size=30,
                color=theme.TEXT_PRIMARY,
            ),
        )
    )


ft.run(main)
