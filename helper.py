from kivymd.app import MDApp


def get_token():
    return MDApp.get_running_app().TOKEN


def update_text(screen, widget_id, message):
    screen.manager.current_screen.ids[widget_id].text = message


def get_text(screen, widget_id):
    return screen.manager.current_screen.ids[widget_id].text


def go_to_screen(screen, id):
    screen.manager.current = id
