

import json 




class Setting:

	def __init__(self, file , name):
		self.name = name 
		self.file  = file


	@property
	def data(self):
		with open(self.file)
		return json.loads()


