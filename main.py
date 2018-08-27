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

'''Login Screen class which consists of login screen and validate username and password
using check_password function'''
class LoginScreen(Screen):
    def check_password(self):
        self.username = 'admin'
        self.password = 'admin'
        if self.ids["Input_Username"].text == str(self.username) and self.ids["Input_Password"].text == str(self.password):
            #print("In Condition")
            self.parent.current = 'UserScreen'
        else:
            print("Incorrect Username or Password")

class UserScreen(Screen):
    pass

class CreateDayData(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

GDR_App = Builder.load_file('GDR.kv')

class GDR(App):
    def build(self):
        return GDR_App

if __name__ == '__main__':
    GDR().run()
