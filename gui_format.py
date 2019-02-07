from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk
from stegano import lsb
from tkinter import messagebox

root=Tk()
tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text="encoding the image")
tabcontrol.add(tab2, text="dEcoding the image")


def browsefunc(widget):
    filename = filedialog.askopenfilename()
    widget.config(text="Path to the File :" + filename)
    widget.insert(0, filename)
def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)

def hide_msg(path,msg):

    hide=lsb.hide(path,msg)
    msg_time=time.asctime().replace(' ','')
    msg_time=msg_time.replace(':','')
    hide.save('secret-pic'+msg_time+'.png')
    messagebox.showinfo("Saved","The image was Succesfully Encrypted and Saved as \nsecret-pic"+msg_time+'.png' )

def decode_image(path):
    print(path)
    msg = lsb.reveal(path)
    messagebox.showinfo("Decoded", "The image was Succesfully Decrypted  \n Showing the mesaage now...")

    #print(" the Secret message is ", msg)
    top=Toplevel(tab2)
    Label(top,text="Message is :"+msg,font=("",16),foreground='green').grid(row=0,column=0)


browsebutton = Button(tab1, text="Browse to Path",width=20,height=1, command= lambda : browsefunc(path_entry))
browsebutton.grid(row=3,column=1,padx=10,pady=10)

path_entry = Entry(tab1,width=40,borderwidth=2,relief="groove")
path_entry.grid(row=2,column=1,padx=10,pady=10)
path_entry.config(font=('Times New Roman',12),)
upload_button=Button(tab1,text="Upload File",foreground="green",command=lambda : select_image(path_entry.get()))
upload_button.grid(row=3,column=2,padx=10,pady=10)
reset_but=Button(tab1,text="Reset",foreground="blue",command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=3,padx=10,pady=10)
Label(tab1,text="Enter your message here: ",font=("",16)).grid(row=4,column=1,padx=10,pady=10)
msg_entry=Entry(tab1,width=40,borderwidth=2,relief='groove',font=("",16))
msg_entry.grid(row=5,column=1,padx=10,pady=10)
enco_but=Button(tab1,text="Hide the Message",font=("",16),foreground="red",command=lambda: hide_msg(path_entry.get(),msg_entry.get()) )
enco_but.grid(row=5,column=2,padx=10,pady=10)
tabcontrol.grid(row=0,column=0)


browsebutton = Button(tab2, text="Browse to Path",width=20,height=1, command= lambda : browsefunc(path_entryd))
browsebutton.grid(row=3,column=1,padx=10,pady=10)

path_entryd = Entry(tab2,width=40,borderwidth=2,relief="groove")
path_entryd.grid(row=2,column=1,padx=10,pady=10)
path_entryd.config(font=('Times New Roman',12),)
decode_button=Button(tab2,text="Decode Image",foreground="red",font=("",18),command=lambda : decode_image(path_entryd.get()))
decode_button.grid(row=3,column=2,padx=10,pady=10)
reset_but=Button(tab2,text="Reset",foreground="blue",command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=3,padx=10,pady=10)

tabcontrol.grid(row=0,column=0)
root.mainloop()
