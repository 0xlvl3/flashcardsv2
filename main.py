# Kivy / GUI.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Screens imports.
from screens import startscreen
from screens import createscreen
from screens import loginscreen
from screens import homescreen
from screens import createdeckscreen
from screens import addflashcardscreen
from screens import inspectdeckscreen
from screens import deletedeckscreen
from screens import playdeckscreen

# Root kv file.
Builder.load_file("kv/frontend.kv")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
