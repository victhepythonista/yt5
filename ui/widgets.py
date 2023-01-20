

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.clock import Clock

from .buttons import IconButton

from notification import AddNotification , RemoveNotification,ReadNotification
from files import icons 
	

class MessageBox(FloatLayout):
	icon = ObjectProperty(None )
	text_box = ObjectProperty(None)

class  NotificationLabel(Label):
	pass



class NotificationBar(FloatLayout):
 	

 	def __init__(self,*args , **kwargs):
 		FloatLayout.__init__(self)
 		Clock.schedule_interval(self.Update , 1)
 		self.text_box = None 
 		self.cache_message = ""

 	def Update(self, interval):
 		# read the latest nottification from  the config 
 		message , level = ReadNotification()

 		if message == self.cache_message: # to save time and resources
 			return
 		if message == "":
 			self.clear_widgets()
 			return 
 		self.clear_widgets()
 		text_box = NotificationLabel()
 		text_box.size_hint = .8,1
 		text_box.pos_hint = {"x":.2, "y":0}

 		text_box.text = message

 		source = "warning96"
 		icon = IconButton(
 			size_hint = (.2,1),
 			pos_hint={"x":0 , "y":0},
 			source = icons[source]
 			
 			)

 		self.add_widget(icon)
 		self.add_widget(text_box)




