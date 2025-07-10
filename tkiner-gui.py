from tkinter import *
from tkinter import Image

from PIL import ImageTk,Image

root = Tk()

root.title('Login form')
root.iconbitmap('favicon.ico')

root.geometry('350x500')
root.configure(background='#0096DC')

img=Image.open('images.png')
resized_img=img.resize((100,100))
img= ImageTk.PhotoImage(resized_img)


img_label=Label(root,image=img)
img_label.pack( pady=(10,10))

img_label=Label(root,text='flipcart' ,fg='white',bg='#0096DC')
img_label.pack()

img_label.config(font=('Arial',24))

email_label=Label(root,text="Enter Email",fg='white',bg='#0096DC')
email_label.pack(pady=(10,5))
email_label.config(font=("Arial",12))
email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text="Password",fg='white',bg='#0096DC')
password_label.pack(pady=(10,5))
password_label.config(font=("Arial",12))
password_label_input=Entry(root,width=50)
password_label_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text="Log in",fg='black',bg='white',width=30,height=3)
login_btn.pack()


root.mainloop()