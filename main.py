import flet as ft


def main(page: ft.Page):
    page.title = "JARVIS X TEST"
    page.bgcolor = "#0A0E14"

    page.add(
        ft.Text(
            "JARVIS X IS RUNNING",
            size=24,
            color="#FFFFFF",
        )
    )


ft.run(main)
