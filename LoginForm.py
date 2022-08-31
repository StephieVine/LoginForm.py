from tkinter import *
from PIL import Image, ImageTk

#window
root = Tk()
root.geometry("700x500+300+150")

def on_entry(e):
    user.delete(0, 'end')

def on_password(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')

def on_enter(e):
    code.delete(0, 'end')

def on_Leave(e):
    password = code.get()
    if password == '':
        code.insert(0, 'Password')

#background________________________________________
root.title("Login System")
image_0=Image.open('C:\\Users\\Igbon Ifijeh\\Desktop\\images ().jpeg')
bck_pic=ImageTk.PhotoImage(image_0.resize((700,500)))

lbl = Label(root, image=bck_pic)
lbl.place(x=1, y=1)

frame=Frame(root, width=300, height=300, bg='floral white')
frame.place(x=30,y=150)

heading =Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Calibre', 23, 'bold'))
heading.place(x=70, y=4)

#user section____________________________________________________________
user=Entry(frame, width=25, fg='black', border=1, bg='white', font=('Harrington', 11, 'bold'))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_entry)
user.bind('<FocusOut>', on_password)

Frame(frame, width=295, height=2,bg='black').place(x=25, y=107)

#password section_______________________________________________________________
code = Entry(frame, width=25, fg='black', border=1, bg='white', font=('Harrington', 11, 'bold'))
code.place(x=30,y=150)
code.insert(0, "password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_Leave)

Frame(frame,width=295, height=2,bg='black').place(x=25, y=177)

#Buttons_______________________________________________
Button(frame, width=30, pady=7, text='Sign in', bg='#57a1f8', fg='white', cursor='hand2', border=0).place(x=35, y=200)

label =Label(frame, text="Don't have an account?", fg='black', bg='white', cursor='hand2', font=('Calibre',9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

#Variable Storage__________________
uservalue = StringVar
codevalue = StringVar

root.mainloop()
