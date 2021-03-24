import random 
from tkinter import*
from PIL import Image, ImageTk
import os

absolute_path = r'C:\Users\Fahima\Desktop\images\ ' # your absolute path goes here(Note: Don't remove the extra space in the end) 

anime = {
"1 Naruto": 'naruto.jpeg' # anime image name
}

root = Tk()
root.geometry("200x100")

def fun():

    top = Toplevel(root)
    top.title('Anime')

    random_choice = random.choice(list(anime.keys())) #choosing random from dictionary keys
    
    label = Label(top, text=random_choice)
    label.pack()

    top.img = ImageTk.PhotoImage(Image.open(os.path.join(absolute_path.strip(),anime[random_choice])))
    
    image_label = Label(top, image=top.img)
    image_label.pack()

can = Canvas(root, height = 100, width = 100)
can.place(relx=0.5, rely=0.5, anchor=CENTER)

b1 = Button(can,text = "Generate",command = fun,activeforeground = "black",activebackground = "yellow",pady=10)
b1.pack(side = TOP)

root.mainloop()