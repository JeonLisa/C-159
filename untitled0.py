from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("Country Flags")
root.geometry("600x600")
root.configure(background="Black")
input_1=Entry(root)
India_flag=ImageTk.PhotoImage(Image.open("India flag.jpg"))
Japan_flag=ImageTk.PhotoImage(Image.open("Japan.png"))
South_Korea_flag=ImageTk.PhotoImage(Image.open("Sk.png"))
mapdic={
        "India":India_flag,
        "Japan":Japan_flag,
        "SouthKorea":South_Korea_flag
        }
def flag():
    try:
        map_name=input_1.get()
        print(map_name)
        label_1["image"]=mapdic[map_name]
    except:
        messagebox.showinfo("Error!","Sorry this country flag doesn't exist in our system")
button_1=Button(root,text="Show Country Flag",command=flag)
label_1=Label(root)
input_1.place(relx=0.5,rely=0.2,anchor=CENTER)
button_1.place(relx=0.5,rely=0.1,anchor=CENTER)
label_1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()