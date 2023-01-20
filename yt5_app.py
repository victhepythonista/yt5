__author__ = "Leting Victor Kipkemboi"

"""

This app was designed and coded by Victor Kipkemboi

email : letingvictorkipkemboi@gmail.com
whatsapp :+254712553793


"""

import sys
import time
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from  kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.logger import Logger
from kivy.clock import Clock
from  kivy.graphics import Line , Canvas , Color ,Rectangle
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty
 
from ui import * 



BASE =  [round(.01*i, 2) for i in range(7,10)]
COLORS  = [(random. choice(BASE), random. choice(BASE), random. choice(BASE), 1) for i in range(226)] 
 

Window.clearcolor = 0,.1,.1,1
 


class YT5App(App):
 


    pass


if __name__  == '__main__':
    YT5App().run()
