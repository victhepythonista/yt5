

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty

from kivy.clock import Clock 

from download import LinkStub 


class LinkStubCard(GridLayout):
	link_title =ObjectProperty(None)
	size_hint_y = .1
	def __init__(self,stub , *args , **kwargs):
		GridLayout.__init__(self )
		self.stub = stub 
		self.deleted =False


	def Update(self):
		self.link_title.text = self.stub.url
		


class LinksContainer(FloatLayout):

	"""

	handles collection of links 

	"""
	link_input =ObjectProperty(None)
	link_stubs_container = ObjectProperty(None)
	def __init__(self, *args , **kwargs):
		FloatLayout.__init__(self )
		self.links = [ f"youtube/Testlink/{i}" for i in range(15)]
		self.started = False
		Clock.schedule_interval(self.CheckStubCards , 2)

	 

	def CheckStubCards(self , interval):
		# check the links for deleted ones 
		update = False
		for card in self.link_stubs_container.children:
			if card.deleted == True :
				self.links.remove(card.stub.url)
				update = True

		if self.started == False:
			self.started = True
			update = True
		if update:self.RefreshLinkStubs()

	def AddLink(self):
		self.AddLinkStub()
	def AddLinkStub(self):
		url = self.link_input.text
		if url.strip() == "":
			return 
		# check if link is valid >>>


		if url in self.links:
			print("LINK ALREADY  added  ")
			self.link_input.text = ""
			return 
		print("adding link ", url )
		self.links.append(url)
		self.RefreshLinkStubs()
		self.link_input.text = ""

	def RemoveLink(self, link):
		if link in self.links:
			self.links.remove(link)

		self.RefreshLinkStubs()


	def RefreshLinkStubs(self):
		if self.links ==[]:
			return
		self.link_stubs_container.clear_widgets()
		sample_card = None
		for l in self.links:
			ls = LinkStub(l)
			card = LinkStubCard(ls)
			card.Update()
			self.link_stubs_container.add_widget(card)
			sample_card = card
		pre = self.link_stubs_container.size
		self.link_stubs_container.size = pre[0] , sample_card.size[1]/2 * len(self.links)
	def GetLinks(self):
		# return the links selected and the quality selected

		pass 




 
	 
 
