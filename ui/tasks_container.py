

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.clock import Clock

from .buttons import IconButton
from  files import icons


class TaskCard(BoxLayout):

	def __init__(self,task , *args , **kwargs ):
		BoxLayout.__init__(self )
		self.task  = task 



class TasksContainer(FloatLayout):

	tasks_box = ObjectProperty(None)
	message_box = ObjectProperty(None)
	def __init__(self, *args , **kwargs ):
		FloatLayout.__init__(self )
		self.container_name = "" # used by taskmanager to assign tasks
		self.tasks =[]
		self.nothing_here_message = ""
		self.i_know_nothings_there = False
		Clock.schedule_interval(self.UpdateTasks , 3 )


	def UpdateTasks(self, interval):
		# update and add task cards 

		if self.tasks == []  :
			if len(self.message_box.children) < 1:
				icon = IconButton()
				label = Label()

				icon.source = icons["desert50"]
				icon.size_hint = 1,.7
				icon.pos_hint = {"x":0,"y":.3}


				label.text = "Nothings here !!"
				label.size_hint = 1,.3
				label.pos_hint = {"x":0,"y":0}

				self.message_box.add_widget(icon)
				self.message_box.add_widget(label)


