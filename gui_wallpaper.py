from tkinter import *
from  tkinter import Image

from PIL import  ImageTk,Image
import  os

def rotation_image():
    global  count
    img_label.config(image=image_array[count%len(image_array)])
    count = count+1
count =1
root = Tk()
root.title('wallpaper')
root.geometry('300x400')
root.configure(bg='skyblue')

files=os.listdir('Wallpaper')

image_array=[]

for file in files:
    img = Image.open(os.path.join('Wallpaper',file))
    reseized_img=img.resize((200,200))
    image_array.append( ImageTk.PhotoImage(reseized_img))
print(image_array)

img_label = Label(root,image=image_array[0])
img_label.pack(pady=(10,10))

next_button = Button(root,text='Next',bg='white',fg='black',width='5',height='1',command=rotation_image)
next_button.pack(pady=(10,10))

root.mainloop()