import flet as ft
from ui import theme
from ui.components import status_dot


class CoreSection:
    def __init__(self):
        self.rotation_angle = 0
        self.timer = None
        self.ring1 = ft.Container(
            width=180,
            height=180,
            border=ft.border.all(2, theme.CYAN_BORDER),
            border_radius=90,
            alignment=ft.alignment.center,
        )
        self.ring2 = ft.Container(
            width=140,
            height=140,
            border=ft.border.all(1, theme.TEXT_MUTED),
            border_radius=70,
            alignment=ft.alignment.center,
        )
        self.core = ft.Container(
            width=80,
            height=80,
            border=ft.border.all(1, theme.AMBER_BORDER),
            border_radius=40,
            alignment=ft.alignment.center,
            content=status_dot("online", size=12),
        )
        self.container = ft.Container(
            content=ft.Stack(
                [self.ring1, self.ring2, self.core],
                alignment=ft.alignment.center,
            ),
            width=200,
            height=200,
            alignment=ft.alignment.center,
            rotate=ft.Rotate(angle=0, alignment=ft.alignment.center),
        )

    def start_rotation(self, page: ft.Page):
        def update_rotation():
            self.rotation_angle = (self.rotation_angle + 1) % 360
            self.container.rotate.angle = self.rotation_angle
            page.update()
        self.timer = ft.Timer(50, update_rotation)
        self.timer.start()

    def stop_rotation(self):
        if self.timer:
            self.timer.cancel()

    def build(self) -> ft.Control:
        return self.container


def create_core_section(page: ft.Page) -> CoreSection:
    core = CoreSection()
    core.start_rotation(page)
    return core
