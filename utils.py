

# useful functions


import requests


def CheckInternet():
    try:
        req = requests.get("https://google.com")
    except requests.ConnectionError:
        return False 
		
    if str(req.status_code)[0] != "2":
        return False 
    
    return True



if __name__ == '__main__':
	CheckInternet() 
	





