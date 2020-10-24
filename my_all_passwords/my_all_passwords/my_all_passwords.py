
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox


pencere = Tk()


pencere.title("My All Passwords")
pencere.geometry("500x500+90+90")
pencere.config(bg="purple")
baslık = Label(pencere,text="My All Passwords",bg="purple", fg="black", font=("Open Sans","30","bold"))
baslık.pack()



password = Label(pencere,text="Enter your password: ",bg="purple", fg="black", font=("Open Sans","15","bold"))
password.place(x=150,y=200)

entry_password= Entry(pencere,show="*")
entry_password.place(x=190,y=250)



def giris():
        if entry_password.get()=="123":
            msg=messagebox.showinfo("Hiiii!!", message="WELCOME")

            all_password = Toplevel()
            all_password.title("My All Passwords")
            all_password.geometry("500x600+590+90")
            all_password.config(bg="purple")

            baslık1 = Label(all_password,text="My All Passwords",bg="purple", fg="black", font=("Open Sans","30","bold"))
            baslık1.pack()

            all = open("all_passwords.txt","r")
            all_passwords=[]
            for x in all:
                all_passwords.append(x.strip())
            all.close()


            inst = Label(all_password,text="Instagram: ",bg="purple", fg="black", font=("Open Sans","20","bold"))
            inst.place(x=20,y=90)
            def instagram():
                msg=messagebox.showinfo("Instagram Password", message=all_passwords[0].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=instagram,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=100)



            inst = Label(all_password,text="Apple: ",bg="purple", fg="black", font=("Open Sans","20","bold"))
            inst.place(x=20,y=150)
            def apple():
                msg=messagebox.showinfo("Apple Password", message=all_passwords[1].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=apple,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=160)



            inst = Label(all_password,text="Facebook: ",bg="purple", fg="black", font=("Open Sans","20","bold"))
            inst.place(x=20,y=210)
            def facebook():
                msg=messagebox.showinfo("Facebook Password", message=all_passwords[2].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=facebook,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=220)



            inst = Label(all_password,text="Hotmail: ",bg="purple", fg="black", font=("Open Sans","20","bold"))
            inst.place(x=20,y=270)
            def hotmail():
                msg=messagebox.showinfo("blabla@hotmail.com Password", message=all_passwords[3].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=hotmail,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=280)



            inst = Label(all_password,text="Gmail: ",bg="purple", fg="black", font=("Open Sans","20","bold"))
            inst.place(x=20,y=330)
            def gmail():
                msg=messagebox.showinfo("blabla@gmail.com Password", message=all_passwords[4].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=gmail,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=340)



            inst = Label(all_password,text="blabla.edu: ",bg="purple", fg="black", font=("Open Sans","18","bold"))
            inst.place(x=20,y=390)
            def yeditepe():
                msg=messagebox.showinfo("blabla.edu.tr Password", message=all_passwords[5].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=yeditepe,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=400)



            inst = Label(all_password,text="Work: ",bg="purple", fg="black", font=("Open Sans","18","bold"))
            inst.place(x=20,y=450)
            def pharmacy():
                msg=messagebox.showinfo("blabla@gmail.com Password", message=all_passwords[6].strip())
            btn_inst = Button(all_password,text="Show",activebackground="green",command=pharmacy,bg='black', fg='white', font=('helvetica', 9, 'bold'))
            btn_inst.place(x=195,y=460)




    

               

btn_giris = Button(pencere,text="OK",activebackground="green",command=giris,bg='black', fg='white', font=('helvetica', 9, 'bold'))
btn_giris.place(x=240,y=300)

mainloop()
