from tkinter import *
import os
creds = 'tempfile.temp'

def Signup():
    global pwordE
    global nameE
    global roots

    roots=Tk()
    roots.title('signup')
    intruction=Label(roots,text='please Enter New Credentals\n')
    intruction.grid(row=0, column=0,sticky=E)

    nameL=Label(roots,text="New Username: ")
    pwordL=Label(roots,text="New Password")
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)

    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)

    signupButton=Button(roots,text='signup',command=FSSignup)
    signupButton.grid(column=1,sticky=W)
    roots.mainloop()

def FSSignup():
    with open(creds,'w') as f:
        f.write(nameE.get())
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

#--------------LOGIN---------------

def Login():
    global nameEL
    global pwordEL
    global rootA

    rootA=Tk()
    rootA.title('Login')
    
    intruction=Label(rootA,text='Please Login\n')
    intruction.grid(row=0,column=0,sticky=E)

    nameL=Label(rootA,text='Username:')
    pwordL=Label(rootA,text='Password:')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)

    nameL=Entry(rootA)
    pwordL=Entry(rootA,show='*')
    nameL.grid(row=1,column=1)
    pwordL.grid(row=2,column=1)

    loginB=Button(rootA,text='Login',command=CheckLogin)
    loginB.grid(columnspan=2,sticky=W)

    rmuser=Button(rootA,text='Delete User',fg='blue',command=DelUser)
    rmuser.grid(columnspan=2,sticky=W)
    rootA.mainloop()



    #----------------check login----------

def CheckLogin():
    with open(creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pword=data[1].rstrip()

        if nameEL.get()==uname and pwordEL.get()==pword:
            r=Tk()
            r.title(':D')
            r.geometry('150x150')
            rlbl=Label(r,text='\n[+] Logged In')
            rlbl.pack()
            r.mainloop()
        else:
            r=Tk()
            r.title('D:')
            r.geometry('150x150')
            rlbl=Label(r,text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()


#-------- Delete User------------

def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    Login()
else:
    Signup()

