from tkinter import *
import random
root = Tk()
root.title("Picnic_bag_list")
root.geometry("400x400")
labeldisplay=Label(root, text="Listed_items: ")
label_randomnumbers=Label(root)
def Picnic():
    display=labeldisplay
    list="Listed Items","Apples","Cookies","Picnic_Blanket", "Unbrella", "Pen", "Tiffin"
    labeldisplay['text'] = str(list)
    ran1=random.randint(1,6)
    label_randomnumbers["text"]="Put item no " + str(ran1) + " in bag"
btn = Button(root,text=" Random number", command= Picnic)  
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_randomnumbers.place(relx=0.5,rely=0.6,anchor=CENTER)
labeldisplay.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()