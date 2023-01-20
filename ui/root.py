from kivy.uix.screenmanager import ScreenManager,FadeTransition
from kivy.clock import Clock

from utils import CheckInternet
from notification import *

class Manager(ScreenManager):


	def __init__(self,*args ,**kwargs):
		ScreenManager.__init__(self)
		self.transition = FadeTransition()
		Clock.schedule_interval(self.CheckInternet , 5)
		self.internet_check_ok = True



	def UpdateTasks(self):
		# update the tasks info 

		pass


	def CheckInternet(self, interval):
		# check the internet connection

		if CheckInternet():
			self.internet_check_ok = True
			RemoveNotification()
			return 
		if not self.internet_check_ok:
			return

		self.internet_check_ok = False

		AddNotification("No internet","warning")



