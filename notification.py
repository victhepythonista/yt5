
from config import notification_config as nc 

def AddNotification(message , level = "basic"  ):
	nc .write("app","message",message)
	nc .write("app","level",level)


def RemoveNotification():
	nc .write("app","message" , "")

def ReadNotification() :
	mess = nc .read("app","message")
	level = nc .read("app","level")
	return mess , level

 
if __name__ == '__main__':
	AddNotification("THIS IS A TEST NOTIFICATION")
