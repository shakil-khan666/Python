class Text(str):
    def duplicate(self):
        return self + self
text =Text("pythonm ")
print(text.duplicate())
