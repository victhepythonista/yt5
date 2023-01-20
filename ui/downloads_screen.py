
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel


class DownloadManager(TabbedPanel):
	def __init__(self, *args ,**kwargs):
		TabbedPanel.__init__(self)


 

class DownloadsScreen(Screen):

 


	def __init__(self, *args ,**kwargs):
		Screen.__init__(self)
		self.pending_downloads_threads =[] # ids to download threads  

	 