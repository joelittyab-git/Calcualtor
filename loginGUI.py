uses = {
    'joeittab@gmail.com':'admin123',
    'xya@yahoo.com':'Xya123',
    'abc@gmail.com':'abc123'
}

def on_submit():
    o = tkinter.PhotoImage(file='C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/icons8-close-window-28.png')
    username = username_entry.get()
    password = password_entry.get()
    b = True
    
    for x in uses.keys():
        if(username==x):b = False
    
    if(b):
        mlabel.configure(
        image = o
        )
        nlabel.configure(
            image = o
        )
    elif(uses[username] != password) :
        mlabel.configure(
            image = o
        )
        nlabel.configure(
            image = o
        )
    else :
        mlabel.configure(
            image = None
        )
        nlabel.configure(
            image = None
        )

            


import tkinter
import customtkinter 

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
main_window = customtkinter.CTk()

def set_window():
    main_window.geometry("1000x750")
    main_window.resizable(False, False)
    main_window.title("Login | User")
def set_mainframe():
    global mainframe
    
    mainframe = customtkinter.CTkFrame(
        master=main_window
    )
    
    mainframe.place(
        relwidth = 1,
        relheight = 1
    )
    
def set_mainframe_components():
    global mainframe, button1,button2,button3,button4
    
    #navigation bar
    navigation_bar = customtkinter.CTkFrame(
        master=mainframe,
        corner_radius=10,
    )
        
    navigation_bar.place(
        relx = 0,
        relheight = 1,
        relwidth = 0.1
    )
    
    #Buttons
    im1 = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/white-home.png')
    button1 = customtkinter.CTkButton(
        master=navigation_bar,
        height=20,
        width=20,
        text="",
        image=im1
    )
    button1.pack(
        pady = (200,0)
    )
    button1.image = im1
    
    im2 = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/l.png')
    button2 = customtkinter.CTkButton(
        master=navigation_bar,
        height=20,
        width=20,
        text="",
        image=im2
    )
    button2.pack(
        pady = (30,0)
    )
    button2.image = im2
    
    
    im3 = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/h.png')
    button3 = customtkinter.CTkButton(
        master=navigation_bar,
        height=20,
        width=20,
        text="",
        image=im3
    )
    button3.pack(
        pady = (30,0)
    )
    button3.image = im3
    
    im4 = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/op.png')
    button4 = customtkinter.CTkButton(
        master=navigation_bar,
        height=20,
        width=20,
        text="",
        image=im4
    )
    button4.pack(
        pady = (30,0)
    )
    button4.image = im4
    
    set_main = customtkinter.CTkFrame(
        master=mainframe
    )
    set_main.place()

def set_login():
    global mlabel, nlabel, password_entry, username_entry
    
    login_frame = customtkinter.CTkFrame(
        master=mainframe,
        height=450,
        width=500,
        bg_color='transparent',
        border_width=2,
        border_color='#1F6AA5'
    )
    login_frame.place(
        relx = 0.29,
        rely = 0.16
    )
    login_frame.pack_propagate(False)
    
    #Componeents
    i = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/icons8-male-user-35.png')
    ilabel = customtkinter.CTkLabel(
        master=login_frame,
        text="",
        image=i
    )
    
    ilabel.place(
        relx = 0.11,
        rely = 0.31
    )
    
    title_label = customtkinter.CTkLabel(
        master=login_frame,
        text="User Login",
        font=('Sans', 20, 'bold'),
        bg_color='black'
        
    )
    
    title_label.place(
        relwidth = 1,
        relheight = 0.1,
        rely = 0,
        
    )
    
    mlabel = customtkinter.CTkLabel(
        master=login_frame,
        text=""
    )
    mlabel.place(
        relx = 0.81,
        rely = 0.32
    )
    
    username_entry = customtkinter.CTkEntry(
        master=login_frame,
        border_width=1,
        border_color='#1F6AA5',
        placeholder_text='Username',
        width=300,
        height=38,
        corner_radius=15
    )
    username_entry.pack(
        pady = (140,0)
    )
    
    nlabel = customtkinter.CTkLabel(
        master=login_frame,
        text=""
    )
    nlabel.place(
        relx = 0.81,
        rely = 0.56
    )
    
    
    k = tkinter.PhotoImage(file = 'C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/p.png')
    klabel = customtkinter.CTkLabel(
        master=login_frame,
        text="",
        image=k
    )
    
    klabel.place(
        relx = 0.11,
        rely = 0.56
    )
    password_entry = customtkinter.CTkEntry(
        master=login_frame,
        border_width=1,
        border_color='#1F6AA5',
        placeholder_text='Password',
        width=300,
        height=38,
        corner_radius=15,
        show="x"
    )
    password_entry.pack( 
        pady = (70,0)
    )
    
    submit_button = customtkinter.CTkButton(
        master=login_frame,
        text='Login',
        font=('Sans-serif', 20, 'bold'),
        command=on_submit
    )
    submit_button.place(
        relheight=0.076,
        relx = 0.33,
        rely = 0.8
    )
    
    
set_window()
set_mainframe()
set_mainframe_components()
set_login()
main_window.mainloop()