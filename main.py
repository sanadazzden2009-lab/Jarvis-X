import flet as ft

import config
from ui import theme


def main(page: ft.Page):
    page.title = config.APP_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = theme.BG_DARK
    page.padding = 0

    page.add(
        ft.Text(
            "STEP 2 - CONFIG AND THEME OK",
            size=24,
            color=theme.TEXT_PRIMARY,
        )
    )


ft.run(main)
