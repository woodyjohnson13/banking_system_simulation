from bank import Bank
from tkinter import *
from PIL import  ImageTk,Image
import os




def main():
    
    #main Screen
    master=Tk()
    master.title("OG Bank")
    
    #functions
    def register():
        #variables
        temp_name=StringVar()
        temp_age=StringVar()
        temp_gender=StringVar()
        temp_password=StringVar()
        
        
        #registration screen
        register_screen=Toplevel(master)
        register_screen.title('Register')
        
        Label(register_screen, text='Please enter your details below to sighn up.', font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
        
        Label(register_screen, text='Name', font=('Calibri,12')).grid(row=1,sticky=W,pady=10)
        
        Label(register_screen, text='Age', font=('Calibri,12')).grid(row=2,sticky=W,pady=10)
        
        Label(register_screen, text='Gender', font=('Calibri,12')).grid(row=3,sticky=W,pady=10)
        
        Label(register_screen, text='Password', font=('Calibri,12')).grid(row=4,sticky=W,pady=10)         
        
        #entries
        Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
        
        Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
        
        Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
        
        Entry(register_screen,textvariable=temp_password).grid(row=4,column=0)
        
    def login():
        print("This is login page")
    
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