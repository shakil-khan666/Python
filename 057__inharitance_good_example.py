class InvalidOparationError(Exception):
    pass
class Stream :
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise InvalidOparationError("steam is always open")
        self.opened = True
        
        
    def close(self):
        if not self.opened:
            raise InvalidOparationError("steam is always closed")
        self.opened = False
    
class FileStream(Stream):
    def Read(self):
        print("reading deta file")
    def Write(self):
        print("wrinting deta file")
        
class NetworkStream(Stream):
    def Read(self):
        print("reading deta file")
    def Write(self):
        print("wrinting deta file")
        
m= FileStream()

m.close()
