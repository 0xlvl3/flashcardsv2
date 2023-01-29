from kivymd.app import MDApp
from kivymd.theming import ThemeManager


def set_theme(screen, theme, primary, accent, hue):
    screen.theme_cls = ThemeManager()
    screen.theme_cls.theme_style = theme
    screen.theme_cls.primary_palette = primary
    screen.theme_cls.accent_palette = accent
    screen.theme_cls.primary_hue = hue


def get_token():
    return MDApp.get_running_app().TOKEN


def update_text(screen, widget_id, message):
    screen.manager.current_screen.ids[widget_id].text = message


def get_text(screen, widget_id):
    return screen.manager.current_screen.ids[widget_id].text


def go_to_screen(screen, id):
    screen.manager.current = id
