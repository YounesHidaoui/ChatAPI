class App :
    # def init api
  
    def __init__(self,api):
        self.api = api
        

    # method get 
    def getapi(self):
        return self.api
    # method set 
    def setapi(self,value):
        if value == '':
            return False
        else:
             self.api= value 
             return True 
    # method str 
    def __str__(self):
        return f"{self.api}"



p = App('hwwle')
p.setapi('')

from pymongo import MongoClient







        