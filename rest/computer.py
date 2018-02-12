import platform
import psutil

class Computer(): 
	def __init__(self): 
		self.name = platform.processor()
		self.disk_usage = psutil.disk_usage('/')
		self.virtual_memory = psutil.virtual_memory() 
		self.cpu_times = psutil.cpu_times() 
		