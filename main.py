from bank import Bank
from tkinter import *
from PIL import  ImageTk,Image
import os




def main():
    
    #main Screen
    master=Tk()
    master.title("OG Bank")
    
    #functions
    def finish_reg():
        name=temp_name.get()
        age=temp_age.get()
        gender=temp_gender.get()
        password=temp_password.get()
        my_balance=balance.get()
        all_accounts=os.listdir()   
        if name=="" or age=="" or gender=="" or password=="":
            notif.config(fg='red',text='All fields required')
            return
        print("Nice to meet you!")
        
        for name_check in all_accounts:
            if name==name_check:
                notif.config(fg='red',text='Account already exists')
                return
            else:
                new_file=open(name,'w')
                new_file.write(name+'\n')
                new_file.write(age+'\n')
                new_file.write(gender+'\n')
                new_file.write(password+'\n')
                new_file.write(my_balance)
                new_file.close()
                notif.config(fg='green',text='Account has been created')
                
                
        
    def register():
        #variables
        global temp_name
        global temp_age
        global temp_gender
        global temp_password
        global balance
        global notif
        
        temp_name=StringVar()
        temp_age=StringVar()
        temp_gender=StringVar()
        temp_password=StringVar()
        balance=StringVar()
        
        
        #registration screen
        register_screen=Toplevel(master)
        register_screen.title('Register')
        
        Label(register_screen, text='Please enter your details below to sighn up.', font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
        
        Label(register_screen, text='Name', font=('Calibri,12')).grid(row=1,sticky=W,pady=10)
        
        Label(register_screen, text='Age', font=('Calibri,12')).grid(row=2,sticky=W,pady=10)
        
        Label(register_screen, text='Gender', font=('Calibri,12')).grid(row=3,sticky=W,pady=10)
        
        Label(register_screen, text='Password', font=('Calibri,12')).grid(row=4,sticky=W,pady=10)
        
        Label(register_screen, text='Balance', font=('Calibri,12')).grid(row=5,sticky=W,pady=10)
        
        
        notif=Label(register_screen,font=('Calibri,12'))
        notif.grid(row=6,sticky=N,pady=10)
        
        #entries
        Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
        
        Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
        
        Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
        
        Entry(register_screen,textvariable=temp_password,show='*').grid(row=4,column=0)
        
        Entry(register_screen,textvariable=balance).grid(row=5,column=0)
        
        
        #buttons
        Button(register_screen,text='Register',command=finish_reg,font=('Calibri',12)).grid(row=6,sticky=N,pady=10)
    
    def login_session():
        #variables
        global login_name
        
        all_accounts=os.listdir()
        login_name=temp_login_name.get()
        login_password=temp_login_password.get()
        
        for name in all_accounts:
            if name==login_name:
                file=open(name,'r')
                file_data=file.read() 
                file_data=file_data.split('\n')
                password=file_data[3]
                if login_password==password:
                    login_screen.destroy()
                    account_dashboard=Toplevel(master)
                    account_dashboard.title('Dashboard')
                    #labels
                    Label(account_dashboard,text='Account Dashboard',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                    
                    Label(account_dashboard,text=f'Welcome,{name}',font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
                    
                    #buttons
                    Button(account_dashboard,text='Personal details',font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    
                    Button(account_dashboard,text='Deposit',font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                    
                    Button(account_dashboard,text='Withdraw',font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                    
                    Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                    
                    return
                else:
                    login_notif.config(fg='red',text='Password incorrect')
                    return
                
        login_notif.config(fg='red',text='No account found')    
               
    def login():
        #variables
        global temp_login_password
        global temp_login_name
        global login_screen
        global login_notif
        
        temp_login_name=StringVar()
        temp_login_password=StringVar()
        
        
        #login screen
        login_screen=Toplevel(master)
        login_screen.title('Login')
        #labels
        Label(login_screen,text='Login to your account',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
        
        Label(login_screen,text='Username',font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
        
        Label(login_screen,text='Password',font=('Calibri',12)).grid(row=2,sticky=N,pady=10)
        
        login_notif=Label(login_screen,font=('Calibri',12))
        login_notif.grid(row=4,sticky=N)
        
        #entries
        Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)  
        
        Entry(login_screen,textvariable=temp_login_password,show='*').grid(row=2,column=1,padx=5) 
        
        #buttons
        Button(login_screen,text='Login',command=login_session,width=15,font=('Calibri',12)).grid(row=3,sticky=N,pady=5,padx=5) 

        
    #image import  
    img=Image.open('main_icon.png')
    img=img.resize((150,150))
    img=ImageTk.PhotoImage(img)
    
    #Labels
    Label(master,text="Welcome to Og Bank",font=("Calibri",20)).grid(row=0,sticky=N,pady=10)
    
    Label(master,text="Most dope bank in the US",font=("Calibri",12)).grid(row=1,sticky=N)
    
    Label(master,image=img).grid(row=2,sticky=N,pady=15)
    
    
    
    #Buttons
    Button(master,text='Register',font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
    
    Button(master,text='Login',font=('Calibri',12),width=20,command=login).grid(row=4,pady=5,sticky=N)
    
    mainloop()

if __name__ == "__main__":
    main()