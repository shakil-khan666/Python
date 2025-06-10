class Text(str):
    def duplicate(self):
        return self + self

class TrackAblelist(list):
    def append(self, object):
        print("appnened called")
        super().append(object)

list = TrackAblelist()
list.append("1")
    
