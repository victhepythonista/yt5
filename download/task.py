


class Task:

	"""

	represents a download ...

	"""
	def __init__(self , stub   , save_path , cache_path , state   ="pending"):
		self.stub = stub 
		self.save_path = save_path 
		self.cache_path = cache_path
		self.state = state 
		self.thread_id = None 



	def Start(self):
		# start  a new thread if thread id is None 
		# restart if thread is dead 


		pass 



	def Completed(self):
		# delete cache  file and clear resources 
		# kill threads


		pass 
		

