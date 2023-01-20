from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from .quality_select import AudioQualitySpinner,VideoQualitySpinner
class HomeScreen(Screen):

	links_container = ObjectProperty(None)

	quality_selector = ObjectProperty(None)
	def __init__(self, *args ,**kwargs):
		Screen.__init__(self)
		self.download_mode ="audio" #video
		  # read from config on startup

		Clock.schedule_interval(self.UpdateQualitySelector ,1)

	def UpdateQualitySelector(self, interval):
		self.SwitchDownloadMode(self.download_mode)
		Clock.unschedule(self.UpdateQualitySelector)


		
	def SwitchDownloadMode(self, mode ):

		print(f"sWITCHED dwonload mode from {self.download_mode} to " , mode)
		self.download_mode = mode

		if  not self.quality_selector:
			return
			
		self.quality_selector.clear_widgets()

		if self.download_mode == "video":
			self.quality_selector.add_widget(VideoQualitySpinner())
		elif self.download_mode == "audio":
			self.quality_selector.add_widget(AudioQualitySpinner())