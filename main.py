import kivy
kivy.require(''+kivy.__version__)

import time
import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

'''Login Screen class which consists of login screen and validate username and password
using check_password function'''
class LoginScreen(Screen):
    def check_password(self):
        self.username = 'admin'
        self.password = 'admin'
        if self.ids["Input_Username"].text == str(self.username) and self.ids["Input_Password"].text == str(self.password):
            print("Logged in Succesfully!")
            self.parent.current = 'UserScreen'
        else:
            print("Incorrect Username or Password")
            content=Label(text="Incorrect Username/Password.Please check and re-enter")
            err_popup = Popup(title="Error Message", size_hint=(None, None), auto_dismiss=True, size=(400, 400), content=content)
            #content.bind(Button(text="close", on_press=err_popup.dismiss))
            err_popup.open()

class UserScreen(Screen):
    pass

class CreateDayData(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class ViewDayData(Screen):
    pass

class ViewReport(Screen):
    pass

GDR_App = Builder.load_file('GDR.kv')

class GDR(App):
    def build(self):
        return GDR_App

if __name__ == '__main__':
    GDR().run()
