import os
import configparser

from defaults import *
 
 

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parser = configparser.ConfigParser()
        if not os.path.isfile(file_path):
            print("CONFIG PATH DOESNT EXIST ")
        self.parser.read(self.file_path)
         
		
    def read( self, section, var ,data_if_none ='' ):
        self.IsSection(section)
        self.IsKey(var , section,data_if_none='')
        data = self.parser[section][var ]
        return data
    

    def write(self,  section, var, data):
        self.IsSection(section)
        self.parser[section][var] = data
        self.SaveConfig()
	
	
    def ListSectionKeys(self, section, evaluate = False):
		#'''return a list of all keys in a section  '''
        self.IsSection(section)
        items_list = (self.parser.items(section))
        data =  list(items_list) 
        keys_list =  [ item[0] for item  in data]
        if evaluate:
            keys_list = [eval(k) for k in keys_list]
        return keys_list
		
        
		
    def ListSections(self):
        # return a list sections
        return self.parser.sections()
	
    def DeleteSection(self, section):
        # delete a section
        if check_section(self.parser, section):
            self.parser.remove_section(section)
            print(section, '   section  deleted !')

			
    def IsSection(self, section):
        if section in self.ListSections():
            return True 
        else:
            self.parser.add_section(section)
            self.SaveConfig()
            return True
        return False

    @property  
    def SectionsNumber(self):
        return len(self.parser.sections())

    def KeysNumber(self, section):
        return len(self.ListSectionKeys(section))

    def SaveConfig(self):
        with open(self.file_path, 'w') as f:
            self.parser.write(f)
            print(type(self).__name__ ,"  configurations saved!\n")
			
		
    def IsKey(self, key, section, data_if_none = ''):
        if  key in self.ListSectionKeys(section):
            return True
        else:
            self.write(section, key, data_if_none)
            self.SaveConfig()
            return True 
		
    
    def ResetData(self,data_dictionary):
        '''
        data dictionary must be of type
        {'section_name':{'key_name':'data',},}
        '''
        for section_name,section_data in data_dictionary.items():
            self.IsSection(section_name)
            for key,data in section_data.items():
                self.write(section_name,key,str(data))
                continue
        print('\n\nConfig file reset complete! \n\n...........................')
			
			
 


app_config = Config('./data/config/app_config.cfg')
notification_config = Config("./data/config/notification_config.cfg")


if __name__ == '__main__':
    app_config.ResetData(APP_CONFIG)
    notification_config.ResetData(NOTIFICATION_CONFIG)