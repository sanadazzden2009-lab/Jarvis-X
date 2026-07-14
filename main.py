import flet as ft

# ---------------------------------------------------------------------------
# Jarvis X - Phase 1: static HUD shell only.
# No AI, no database, no networking, no providers, no memory, no APIs.
# Every color below is a plain hex string and every spacing value is a plain
# int - no with_opacity / padding.only / border helpers - to stay on the API
# surface already confirmed working in Phase 0.
# ---------------------------------------------------------------------------

BG_DARK = "#0A0E14"
BG_HEADER = "#0F1621"
DRAWER_BG = "#0D1219"
PANEL_JARVIS = "#132229"
PANEL_USER = "#241D12"
PANEL_INPUT = "#131A24"
CYAN = "#4FD8E8"
CYAN_BORDER = "#2A6570"
AMBER = "#FFB454"
AMBER_BORDER = "#8A6428"
TEXT_PRIMARY = "#E7EEF5"
TEXT_MUTED = "#66798D"
HAIRLINE = "#1C2733"


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
                ft.Text(text, size=14, color=TEXT_PRIMARY),
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
            ft.Icon(icon, size=18, color=TEXT_MUTED),
            ft.Text(label, size=13, color=TEXT_PRIMARY),
        ],
        spacing=12,
    )


def main(page: ft.Page):
    page.title = "Jarvis X"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG_DARK
    page.padding = 0

    # ---- Header -----------------------------------------------------------
    status_dot = ft.Container(width=8, height=8, border_radius=4, bgcolor=CYAN)

    header = ft.Container(
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("JARVIS X", size=20, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                        ft.Row([status_dot, ft.Text("ONLINE", size=11, color=TEXT_MUTED, weight=ft.FontWeight.BOLD)], spacing=6),
                        ft.Text("Provider: \u2014   Model: \u2014   Latency: \u2014", size=10, color=TEXT_MUTED),
                    ],
                    spacing=4,
                ),
                ft.IconButton(ft.Icons.MENU, icon_color=TEXT_PRIMARY, on_click=lambda e: toggle_drawer(e)),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=18,
        bgcolor=BG_HEADER,
    )

    # ---- Drawer -------------------------------------------------------------
    drawer_items = [
        (ft.Icons.ADD, "New Chat"),
        (ft.Icons.HISTORY, "Conversation History"),
        (ft.Icons.STAR_BORDER, "Memory"),
        (ft.Icons.SETTINGS, "Settings"),
        (ft.Icons.SPEED, "Diagnostics"),
        (ft.Icons.CLOUD, "Providers"),
        (ft.Icons.FOLDER, "Downloads"),
        (ft.Icons.INFO, "About"),
    ]

    drawer = ft.Container(
        content=ft.Column(
            [ft.Text("MENU", size=11, color=TEXT_MUTED, weight=ft.FontWeight.BOLD)]
            + [menu_item(icon, label) for icon, label in drawer_items],
            spacing=22,
        ),
        width=210,
        bgcolor=DRAWER_BG,
        padding=20,
        visible=False,
    )

    def toggle_drawer(e):
        drawer.visible = not drawer.visible
        page.update()

    # ---- AI core section ----------------------------------------------------
    core_circle = ft.Container(width=90, height=90, border_radius=45, bgcolor=CYAN)

    core_section = ft.Column(
        [
            ft.Container(height=30),
            core_circle,
            ft.Container(height=14),
            ft.Text("AWAITING YOUR COMMAND", size=12, color=TEXT_MUTED, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ---- Chat view (demo content only, not wired to anything) ---------------
    chat_view = ft.ListView(
        controls=[
            message_bubble("YOU", "Show me the new interface", AMBER, PANEL_USER, AMBER_BORDER, True),
            message_bubble("JARVIS", "Static UI online. Backend arrives in a later phase.", CYAN, PANEL_JARVIS, CYAN_BORDER, False),
        ],
        expand=True,
        spacing=14,
        padding=16,
    )

    # ---- Input bar ------------------------------------------------------------
    user_input = ft.TextField(
        hint_text="Ask Jarvis...",
        color=TEXT_PRIMARY,
        border_color="transparent",
        focused_border_color="transparent",
        bgcolor="transparent",
        expand=True,
    )

    input_bar = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(ft.Icons.IMAGE, icon_color=TEXT_MUTED, tooltip="Attach image"),
                ft.IconButton(ft.Icons.ATTACH_FILE, icon_color=TEXT_MUTED, tooltip="Attach file"),
                ft.IconButton(ft.Icons.MIC, icon_color=TEXT_MUTED, tooltip="Voice"),
                ft.IconButton(ft.Icons.CAMERA_ALT, icon_color=TEXT_MUTED, tooltip="Camera"),
                user_input,
                ft.IconButton(ft.Icons.SEND, icon_color=CYAN, tooltip="Send"),
            ],
            spacing=2,
        ),
        bgcolor=PANEL_INPUT,
        border_radius=16,
        padding=6,
        margin=16,
    )

    # ---- Assemble -------------------------------------------------------------
    main_column = ft.Column(
        [core_section, ft.Container(content=chat_view, expand=True), input_bar],
        expand=True,
        spacing=0,
    )

    body = ft.Row(
        [drawer, main_column],
        expand=True,
        spacing=0,
    )

    divider = ft.Container(height=1, bgcolor=HAIRLINE)

    page.add(
        ft.Column([header, divider, body], expand=True, spacing=0)
    )


ft.run(main)
