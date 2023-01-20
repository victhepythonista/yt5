

class LinkStub:

	"""
	contains info on a link , file type ,quality ..etc 

	"""
	def __init__(self , url , file_type  =".mp4" ):
		self.url = url 
		self.file_type = file_type
		self.download_location = ""
		self.quality  = ""
