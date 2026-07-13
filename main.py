import sys
import platform
from importlib.metadata import version as pkg_version

print("Application starting...")
print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")

try:
    flet_version = pkg_version("flet")
except Exception as e:
    flet_version = f"unknown ({e})"
print(f"Flet: {flet_version}")

import flet as ft


def main(page: ft.Page):
    print("main() entered")

    page.title = "Jarvis X"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0A0E14"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("JARVIS X", size=32, weight="bold", color="#E7EEF5"),
        ft.Text(f"Python {sys.version.split()[0]}", size=12, color="#66798D"),
        ft.Text(f"Flet {flet_version}", size=12, color="#66798D"),
        ft.Text(platform.platform(), size=12, color="#66798D"),
    )

    print("UI rendered")


print("Calling ft.run...")
ft.run(main)
