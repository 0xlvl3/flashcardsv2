from kivymd.app import MDApp


def switch_theme(screen, current_theme):
    if current_theme == "Dark":
        print("DDDarrrk")
        screen.theme_cls.theme_style = "Dark"
    else:
        print("Lightttt")
        screen.theme_cls.theme_style = "Light"


def get_token():
    """
    Function gets the user token that is currently using the application.
    """
    return MDApp.get_running_app().TOKEN


def show_button(screen, hide_btn_id, show_btn_id):
    """
    Function will be used within play screen to show the buttons one at a time.
    """
    screen.ids[hide_btn_id].opacity = 0
    screen.ids[show_btn_id].opacity = 1


def update_text(screen, widget_id, message):
    """
    Function will update a screens text.
    """
    screen.manager.current_screen.ids[widget_id].text = message


def get_text(screen, widget_id):
    """
    Function will get the input of an id given.
    """
    return screen.manager.current_screen.ids[widget_id].text


def go_to_screen(screen, id):
    """
    Function will take current screen it is on and then switch to the id given.
    """
    screen.manager.current = id
