


from kivy.uix.button import Button 
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.image import Image
from kivy.uix.label import Label
from files import icons


class IconButton(ButtonBehavior , Image):

 
	pass 

class NavButton(ButtonBehavior , Label):
	def on_mouse_pos(self, instance):
		print("mouse pos")
	pass

class ModeButton(Button):

	def on_kv_post(self , instance):
		self.background_color  = 0,0,.5,1
	def SwitchColor(self, homescreen , mode ):
		if homescreen.download_mode == mode:
			self.background_color = (.3,1,.6,1)
		else:
			self.background_color = 0,0,.5,1