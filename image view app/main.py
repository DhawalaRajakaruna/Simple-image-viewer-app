import os
from tkinter import*
from PIL import ImageTk,Image
from os import listdir
 
root=Tk()
root.title("Image view App")

image_names=[]
for images in os.listdir("images"):
    image_names.append(images)

def backward():
    global i
    if i>0:
        label.grid_forget()
        i-=1
        loadimage(image_names[i],i)

def forward():
    global i
    if i<len(image_names)-1:
        label.grid_forget()
        i+=1
        loadimage(image_names[i],i)
        

def loadimage(name,i):
    try:
        global label
        label=Label(root)
        label.grid(row=0,columnspan=3,pady=50,padx=100)
        img=ImageTk.PhotoImage(Image.open('images/{}'.format(name)))
        label.config(image=img)
        label.image=img

        st="Image {} of {} ".format(i+1,len(image_names))
        indexlabel=Label(root,text=st,justify="right",bd=1,relief=SUNKEN)
        indexlabel.grid(row=2,column=0,columnspan=3)
    except Exception as e:
        print(e)

i=0
loadimage(image_names[i],i)

exit_but=Button(root,text='Exit',command=root.quit).grid(row=1,column=1)
global backward_but
global forward_but
backward_but=Button(root,text='<<',command=lambda:backward()).grid(row=1,column=0)
forward_but=Button(root,text='>>',command=lambda:forward()).grid(row=1,column=2)

root.mainloop()
