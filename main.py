from tkinter import *
from tkinter.messagebox import *
import random,string
import pyperclip


def generator():

		small_alpha=string.ascii_lowercase
		caps_alpha=string.ascii_uppercase
		numbers=string.digits
		special=string.punctuation
		all=small_alpha+caps_alpha+numbers+special
	
		pass_len=int(len_box.get())
		
		if choice.get()==1:
			p=random.sample(small_alpha,pass_len)
			ent.configure(text=p)

		if choice.get()==2:
			q=random.sample(small_alpha+caps_alpha,pass_len)
			ent.configure(text=q)

		if choice.get()==3:
			r=random.sample(all,pass_len)
			ent.configure(text=r)
	


def copy():
	a=ent.cget("text")
	pyperclip.copy(a)
	showinfo("Success","Password copied to clipboard")




root=Tk()
root.geometry("500x700+400+30")
root.title("Password Generator")
root.config(bg='gray20')
choice=IntVar()
f=("arial",13,"bold")


pass_label=Label(root,text="Random Password Generator",font=("times new roman",20,"bold"),bg="gray20",fg="white")
pass_label.pack(pady=15)
weak=Radiobutton(root,text="Weak",value=1,variable=choice,font=f)
weak.pack(pady=14)
med=Radiobutton(root,text="Medium",value=2,variable=choice,font=f)
med.pack(pady=14)
str=Radiobutton(root,text="Strong",value=3,variable=choice,font=f)
str.pack(pady=14)
pass_len=Label(root,text="Password length",font=("times new roman",20,"bold"),bg="gray20",fg="white")
pass_len.pack(pady=14)
len_box=Spinbox(root,from_=5,to_=18,width=5,font=f)
len_box.pack(pady=14)
btn=Button(root,text="Generate",font=f,command=generator)
btn.pack(pady=14)
ent=Label(root,width=25,bd=2,font=f)
ent.pack(pady=14)
cpy=Button(root,text="Copy to Clipboard",font=f,command=copy)
cpy.pack(pady=14)


root.mainloop()