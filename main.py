# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from fire_admin import logout

# Screens imports.
from screens.startscreen import kv_startscreen
from screens import createscreen
from screens import homescreen
from screens import createdeckscreen
from screens import addflashcardscreen
from screens import inspectdeckscreen
from screens import deletedeckscreen
from screens import playdeckscreen
from screens import loginscreen
from screens.loginscreen import LoginScreen

# Root kv file.
Builder.load_string(kv_startscreen)
Builder.load_file("kv/frontend.kv")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()

    def on_stop(self):
        home_screen = self.root.get_screen("home_screen")
        user_token = home_screen.token
        print(f"This is from the log out screen: logged out: {user_token}")
        logout(user_token)


MainApp().run()
