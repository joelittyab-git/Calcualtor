import tkinter
from tkinter import Frame
from tkinter import Label
from tkinter import Button
import math
import customtkinter

main_window = tkinter.Tk()

#window constants
background_color ='#1C1C1C'
button_height = 3
button_width = 9

button1_color = '#505050'
button2_color = '#FF9500'
button3_color = '#D4D4D2'

view_prev_frame_button = None

#Caculation 
number_list = []
operations_list = ['+']
current_number = ''

def on_number_button_click(s):
    global current_number
    
    display_label.delete(0,tkinter.END)
    try:
        n = s[0:6]
    except:
        print("<n")
        n = ''

    
    if(n!='cos(x)' or n!='sin(x)', n!='tan(x)', n!='csc(x)'):
        current_number= current_number+str(s)
    else:
        n = s[0:6]
        print(n)
        number_list.append(n)
        display_label.delete(0,tkinter.END)
        current_number=''
    display_label.insert(0,current_number)
    
def on_operator_click(o):
    global current_number
    
    
    if(display_label.get() == 'x' or display_label.get() == '-' or
       display_label.get() == '+' or display_label.get() == '/' or
       display_label.get() == '='):
        
        display_label.delete(0, tkinter.END)
        display_label.insert(0, o)
        operations_list.pop()
        operations_list.append(o)
        print(operations_list)
        print(number_list)
    
    else:
        try:
            number_list.append(float(current_number))
        except:
            number_list.append(current_number)
        display_label.delete(0, tkinter.END)
        display_label.insert(0, o)
        operations_list.append(o)
        current_number = ''
        
            
            
        print(operations_list)
        print(number_list)

def on_result_clicked():
    global current_number
    
    #adding the recent number
    try:
        number_list.append(float(current_number))
    except:
        number_list.append((current_number))
        
    display_label.delete(0, tkinter.END)
    current_number = ''
    print(operations_list)
    print(number_list)
    
    
    print(number_list)
    print(operations_list)
    
    result = 0
    current_number = 0.0
    on_result_clicked.trig_encounter_index = 0
    on_result_clicked.trig = False
    on_result_clicked.trig_prior_operator = ''
    
    
    for x in range(0,len(number_list)):
        current_number = number_list[x]
        
        try:
            if(number_list[x]=='sin(x)' or number_list[x]=='cos(x)' or number_list[x]=='tan(x)' or
                number_list[x]=='csc(x)' or number_list[x]=='sec(x)' or number_list[x]=='cot(x)'):
                on_result_clicked.trig = True
                on_result_clicked.trig_encounter_index = x
                on_result_clicked.trig_prior_operator = operations_list[x]
                break
            
            elif(operations_list[x]=='x'):
                result*=current_number
            elif(operations_list[x]=='+'):
                result+=current_number
            elif(operations_list[x]=='-'):
                result -= current_number
            elif(operations_list[x]=='/'):
                result /= current_number
        except:
            print("Something went wrong")
        
        
        #if trig was encountered        
        if(on_result_clicked.trig):
            trig_result = 0
            for i in range(len(number_list), on_result_clicked.trig_encounter_index, i=i-1):
                if(number_list[x]=='x'):
                    trig_result*=current_number
                elif(number_list[x]=='+'):
                    trig_result+=current_number
                elif(number_list[x]=='-'):
                    retrig_resultsult -= current_number
                elif(number_list[x]=='/'):
                    trig_result /= current_number
                elif(number_list[x]=='sin(x)'):
                    trig_result = math.sin(trig_result)
                elif(number_list[x]=='cot(x)'):
                    trig_result = math.cot(trig_result)
                elif(number_list[x]=='tan(x)'):
                    trig_result = math.tan(trig_result)
                elif(number_list[x]=='csc(x)'):
                    trig_result = 1.0/math.sin(trig_result)
                elif(number_list[x]=='sec(x)'):
                    trig_result = 1.0/math.cos(trig_result)
                elif(number_list[x]=='cot(x)'):
                    trig_result = 1.0/math.tan(trig_result)
            
            #final result after trig calculation
            if(on_result_clicked.trig_prior_operator=='+'):
                result = result + trig_result
            if(on_result_clicked.trig_prior_operator=='-'):
                result = result - trig_result
            if(on_result_clicked.trig_prior_operator=='/'):
                result = result / trig_result
            if(on_result_clicked.trig_prior_operator=='*'):
                result = result * trig_result
            
    
    #display result in the main calc display
    display_label.insert(0, result)
    
def clear_result_box():
    global current_number, display_label
    
    operations_list.clear()
    operations_list.append('+')
    number_list.clear()
    current_number = ''
    display_label.delete(0, tkinter.END)
    print(number_list)
    print(operations_list)


def on_trigoperator_click(o):
    global current_number
    
    if(display_label.get() == 'x' or display_label.get() == '-' or
       display_label.get() == '+' or display_label.get() == '/' or
       display_label.get() == '='):
        
        display_label.delete(0, tkinter.END)
        display_label.insert(0, o)
        operations_list.pop()
        operations_list.append(o)
        print(operations_list)
        print(number_list)
    
    else:
        number_list.append(float(current_number))
        display_label.delete(0, tkinter.END)
        display_label.insert(0, o)
        operations_list.append(o)
        current_number = ''
        print(operations_list)
        print(number_list)
    

def set_main_window():
    main_window.resizable(False, False)
    main_window.title("Calculator")
    main_window.geometry("300x400")
    main_window.configure(
        bg=background_color
    )
    
def set_disaply_frame():
    global display_frame, display_label
    
   
    
    display_frame = Frame(
        master=main_window,
        height=80,
        width=300,
        background=background_color
    )
    display_frame.pack_propagate(False)
    display_frame.grid_propagate(False)
    
    display_frame.pack(
        pady=(6,8)
    )
    
    display_label = tkinter.Entry(
        master=display_frame,
        background=background_color,
        foreground='white',
        font=('Sans-Serif',39,'bold'),
        justify='right',
        text="112",
        borderwidth=0,
        disabledbackground=background_color
    )
    display_label.place(
        relheight=1,
        relwidth=1
    )
    display_label.justify = 'right'
    display_label.insert(0,"0")
    
def set_button_frame():
    global button_frame
    
    button_frame = tkinter.Frame(
        master=main_window,
        bg=background_color,
        width=300,
        height=320
    )
    button_frame.pack()
    
    button_frame.grid_propagate(False)
    button_frame.pack_propagate(False)
    
def set_button_frame_component():
    global main_window, next_frame_button
    
    for component in button_frame.winfo_children():
        component.destroy()
        
    if(view_prev_frame_button!=None):
        view_prev_frame_button.destroy()
    
    img = tkinter.PhotoImage(file="C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/icons8-next-64.png")
    next_frame_button = Button(
        master=main_window,
        height=20,
        width=50,
        image=img,
        foreground='white',
        font=('Sans-Serif',13,'bold'),
        borderwidth=0,
        background=background_color,
        activebackground='black',
        command=change_button_frame
   
    )
    next_frame_button.place(
        relx=0.009,
        rely=0.05
    )
    next_frame_button.image = img
    
    button1 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='AC',
        borderwidth=0,
        command=clear_result_box
    )
    button1.grid(
        row=0,
        column=0,
        padx=(7,2)
    )
    
    button2 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="+/-",
        borderwidth=0,
        foreground='white'
    )
    button2.grid(
        row=0,
        column=1,
        padx=2
    )
    
    button3 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="%",
        borderwidth=0,
        foreground='white'
    )
    button3.grid(
        row=0,
        column=2,
        padx=2
    )
    
    button4 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="/",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('/')
    )
    button4.grid(
        row=0,
        column=3,
        padx=2
    )
    
    button5 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='1',
        borderwidth=0,
        command=lambda:on_number_button_click(1)
    )
    button5.grid(
        row=1,
        column=0,
        padx=(7,2)
    )
    
    button6 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="2",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(2)
    )
    button6.grid(
        row=1,
        column=1,
        padx=2
    )
    
    button7 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="3",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(3)
    )
    button7.grid(
        row=1,
        column=2,
        padx=2
    )
    
    button8 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="x",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('x')
    )
    button8.grid(
        row=1,
        column=3,
        padx=2,
        pady=3
    )
    
    button9 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='4',
        borderwidth=0,
        command=lambda:on_number_button_click(4)
    )
    button9.grid(
        row=2,
        column=0,
        padx=(7,2)
    )
    
    button10 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="5",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(5)
    )
    button10.grid(
        row=2,
        column=1,
        padx=2
    )
    
    button11 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="6",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(6)
    )
    button11.grid(
        row=2,
        column=2,
        padx=2
    )
    
    button12 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="-",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('-')
    )
    button12.grid(
        row=2,
        column=3,
        padx=2
    )
    
    button13 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='7',
        borderwidth=0,
        command=lambda:on_number_button_click(7)
    )
    button13.grid(
        row=3,
        column=0,
        padx=(7,2)
    )
    
    button14 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="8",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(8)
    )
    button14.grid(
        row=3,
        column=1,
        padx=2
    )
    
    button15 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="9",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(9)
    )
    button15.grid(
        row=3,
        column=2,
        padx=2
    )
    
    button16 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="+",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('+')
    )
    button16.grid(
        row=3,
        column=3,
        padx=2,
        pady=3
    )
    
    button17 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width*2+1,

        height=button_height,
        text="0",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(0)
    )
    button17.grid(
        row=4,
        column=0,
        padx=(8,0),
        columnspan=2
    )
    
    button17 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text=".",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click(".")
    )
    button17.grid(
        row=4,
        column=2,
        pady=0
    )
    
    button18 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="=",
        borderwidth=0,
        foreground='white',
        command=on_result_clicked
    )
    button18.grid(
        row=4,
        column=3,
        padx=1,
        pady=1
    )
    
def change_button_frame():
    global next_frame_button,view_prev_frame_button
    
    #clearing button frame
    for x in button_frame.winfo_children():
        x.destroy()
    next_frame_button.destroy()
    
    #adding move page button
    img = tkinter.PhotoImage(file='C:/Users/joeli/Main/Desktop/Projects/Python/H60-Course/Session06/prev.png')

    view_prev_frame_button = Button(
        master=main_window,
        image= img,
        text='Helol',
        font=('Sans-serif',20,'normal'),
        height=26,
        width=20,
        foreground='white',
        activebackground='black',
        borderwidth=0,
        background=background_color,
        command=set_button_frame_component
    )
    view_prev_frame_button.place(
        relx=0.06,
        rely=0.03
    )
    view_prev_frame_button.image = img
    
    
    
    button1 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='AC',
        borderwidth=0,
        command=clear_result_box
    )
    button1.grid(
        row=0,
        column=0,
        padx=(7,2)
    )
    
    button2 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="+/-",
        borderwidth=0,
        foreground='white'
    )
    button2.grid(
        row=0,
        column=1,
        padx=2
    )
    
    button3 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="%",
        borderwidth=0,
        foreground='white'
    )
    button3.grid(
        row=0,
        column=2,
        padx=2
    )
    
    button4 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="/",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('/')
    )
    button4.grid(
        row=0,
        column=3,
        padx=2
    )
    
    button5 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        foreground='white',
        text='sin(x)',
        borderwidth=0,
        command=lambda:on_number_button_click('sin(x)')
    )
    button5.grid(
        row=1,
        column=0,
        padx=(7,2)
    )
    
    button6 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="cos(x)",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click('cos(x)')
    )
    button6.grid(
        row=1,
        column=1,
        padx=2
    )
    
    button7 = Button(
        master=button_frame,
        background=button1_color,
        width=button_width,
        height=button_height,
        text="tan(x)",
        borderwidth=0,
        foreground='white',
        command=lambda:on_number_button_click('tan(x)')
    )
    button7.grid(
        row=1,
        column=2,
        padx=2
    )
    
    button8 = Button(
        master=button_frame,
        background=button2_color,
        width=button_width,
        height=button_height,
        text="x",
        borderwidth=0,
        foreground='white',
        command=lambda:on_operator_click('x')
    )
    button8.grid(
        row=1,
        column=3,
        padx=2,
        pady=3
    )
    
    
def main():
    set_main_window()
    set_disaply_frame()
    set_button_frame()
    set_button_frame_component()
    
main()
main_window.mainloop()