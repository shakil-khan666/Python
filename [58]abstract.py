from abc import ABC ,abstractmethod
class InvalidOparationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    def open(self):
        if  self.opened:
            raise InvalidOparationError("steam already open")
        self.opened = True
    def close(self):
        if  self.opened:
            raise InvalidOparationError("steam already close")
        self.opened = False
        
        
    @abstractmethod()
    def read(self):
        pass  
class FileStream:
    def read(self):
        print("reading")
    def writing(self):
        print("writing")
class NetworkSteam:
    def read(self):
        print("reading")
    def writing(self):
        print("writing")
class MemoryStream():
    def read(self):
        print ("read a memory")

stream  = MemoryStream()

stream.open()
    
    
        
         
         