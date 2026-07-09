
# create a multi tasking password manager

import tkinter as tk

import random

letters = "abcdefghijklmnopqrstuvwxyz1234567890@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ"


window = tk.Tk()


window.geometry("700x500")

window.configure(bg="black")

window.title("PASS PRO")


def store():

    
    website = entry.get()

    username = entry1.get()

    password = entry2.get()

    f = open("password.txt","a")

    f.write(f"WEBSITE = {website}\n")

    f.write(f"USERNAME = {username}\n")

    f.write(f"PASSWORD = {password}\n\n")

    f.close()
    

def delete():

    entry.delete(0,tk.END)

    entry1.delete(0,tk.END)

    entry2.delete(0,tk.END)


# this part is the only hard one

def find():

    website = entry.get()

    found = False

    with open("password.txt","r") as f:

        lines = f.readlines()

    for i in range(len(lines)):


        if lines[i].strip() == f"WEBSITE = {website}" :

            username = lines[i + 1].replace("USERNAME = ", "").strip()

            password = lines[i + 2].replace("PASSWORD = ", "").strip()


            entry1.delete(0,tk.END)

            entry2.delete(0,tk.END)

            entry1.insert(0,username)

            entry2.insert(0,password)
            
            found = True

            break

    if not found:

            
            entry1.delete(0,tk.END)

            entry2.delete(0,tk.END)

            entry1.insert(0,"NOT FOUND")

            entry2.insert(0,"NOT FOUND")



hidden = True

def safe():

    global hidden

    if hidden:

        entry2.config(show="")
        hidden = False

    else:

        entry2.config(show="*")

        hidden = True



def generator():

    password = ""

    for i in range(14):

        password = password + random.choice(letters)


    entry2.delete(0, tk.END)

    entry2.insert(0, password)



entry = tk.Entry(window,width=25,font=("Arial",14),bg="white",fg="blue")

entry.grid(row=0,column=1)

entry1 = tk.Entry(window,width=23,font=("Arial",14),bg="white",fg="blue")

entry1.grid(row=1,column=1)

entry2 = tk.Entry(window,width=25,font=("Arial",17),bg="white",fg="blue", show="*")

entry2.grid(row=2,column=1)


buttonsave = tk.Button(window,text="SAVE",command=store,font=("Arial",10),bg="yellow")

buttonsave.grid(row=3,column=1)

buttonsearch = tk.Button(window,text="SEARCH",command=find,font=("Arial",10),bg="yellow")

buttonsearch.grid(row=5,column=1)

buttongpass = tk.Button(window,text="GENERATE PASSWORD",command=generator,font=("Arial",10),bg="yellow")

buttongpass.grid(row=7,column=1)

buttonshpass = tk.Button(window,text="SHOW/HIDE PASSWORD",command=safe,font=("Arial",10),bg="yellow")

buttonshpass.grid(row=6,column=1)

buttonshclear = tk.Button(window,text="CLEAR",command=delete,font=("Arial",10),bg="yellow")

buttonshclear.grid(row=4,column=1)





label = tk.Label(window,text= "WEBSITE",font=("arial",20),width=10,height=3,bg="lightblue")

label.grid(row=0,column=0)

label = tk.Label(window,text= "USERNAME/EMAIL",font=("arial",20),width=20,height=3,bg="lightblue")

label.grid(row=1,column=0)

label = tk.Label(window,text= "PASSWORD",font=("arial",20),width=10,height=3,bg="lightblue")

label.grid(row=2,column=0)




window.mainloop()
