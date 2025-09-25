from tkinter import *
root= Tk()
root.title("Calculator for github")
frame= Frame(root)
frame.pack(fill="both", expand=1)


#--------------------funcion pulsar numbers------------------------ 

def pressNumbers(num):
    
    global reset_screen  
    global operator1    
    global operator2

    if reset_screen== True:
        numberScreen.set(num)
        reset_screen= False

    elif numberScreen.get() == "0":
        numberScreen.set(num)

    else:                                               
        numberScreen.set( numberScreen.get() + num)   

    
    if op2_mode==True:
        operator2= float(numberScreen.get())

    



#------------------------------no mas de una coma---------------------

counter=0          

def pressComma():
    
    global counter

    if counter <1:
        numberScreen.set(numberScreen.get() + ".")
        counter+=1


#------------------------boton desacer--------------------------------


def undo():
    
    global operator1
    global operator2
    lista= []
  
    for i in numberScreen.get():
        lista.append(i)
    try:    
        lista.pop()
    except:
        IndexError
    
    if op2_mode==False:
        operator1= "".join(lista)
        numberScreen.set(operator1)
    elif op2_mode==True:
        operator2= "".join(lista)
        numberScreen.set(operator2)


#---------------------boton C, borrar-----------------------------------

def deleteEverything():

    global operation
    global counter
    global operator1
    global operator2
    global op2_mode
    global reset_screen
    global result

    operation= ""
    counter= 0
    operator1= ""
    operator2= ""
    op2_mode= False
    reset_screen= False
    result= ""
    numberScreen.set("0")



#---------------------funcion addition-----------------------

def addition():

    global operation
    global result
    global counter
    global reset_screen
    global operator1
    global operator2
    global op2_mode


    if op2_mode==False:
        operator1= float(numberScreen.get())

    if operation=="substraction":
        substraction()
    elif operation=="multiplication":
        multiplication()
    elif operation=="division":
        division()
    elif operation=="power_of":
        power_of()
    
    elif operator1!='' and operator2!='':
        result= operator1 + float(operator2)
        numberScreen.set(result)
        operator1= result
        operator2= ''
        
    
        
    operation= "addition"

    counter= 0
    reset_screen= True
    op2_mode= True


#-----------------------funcion substraction-----------------------------

def substraction():
    
    global operation
    global result
    global counter
    global reset_screen
    global operator1
    global operator2
    global op2_mode

    if op2_mode==False:
        operator1= float(numberScreen.get())

    if operation=="addition":
        addition()
    elif operation=="multiplication":
        multiplication()
    elif operation=="division":
        division()
    elif operation=="power_of":
        power_of()
    
    elif operator1!='' and operator2!='':
        result= operator1 - float(operator2)
        numberScreen.set(result)
        operator1= result
        operator2= ''
        
    operation= "substraction"

    counter= 0
    reset_screen= True
    op2_mode= True





#-------------------------funcion multiplication--------------------

multiplicado=''
multiplicador=''

def multiplication():
    
    global operation
    global result
    global counter
    global reset_screen
    global operator1
    global operator2
    global op2_mode

    

    if op2_mode==False:
        operator1= float(numberScreen.get())

    if operation=="addition":
        addition()
    elif operation=="substraction":
        substraction()
    elif operation=="division":
        division()
    elif operation=="power_of":
        power_of()
    
    elif operator1!='' and operator2!='':
        result= operator1 * float(operator2)
        numberScreen.set(result)
        operator1= result
        operator2= ''
        
    operation= "multiplication"

    counter= 0
    reset_screen= True
    op2_mode= True


#-------------------------funcion dvision--------------------------

def division():
    
    global operation
    global result
    global counter
    global reset_screen
    global operator1
    global operator2
    global op2_mode

    
    if op2_mode==False:
        operator1= float(numberScreen.get())

    if operation=="addition":
        addition()
    elif operation=="multiplication":
        multiplication()
    elif operation=="substraction":
        substraction()
    elif operation=="power_of":
        power_of()
    
    elif operator1!='' and operator2!='':
        result= operator1 / float(operator2)
        numberScreen.set(result)
        operator1= result
        operator2= ''
        
    operation= "division"

    counter= 0
    reset_screen= True
    op2_mode= True


#------------------------funcion pootencia---------------------------

def power_of():

    global operation
    global result
    global counter
    global reset_screen
    global operator1
    global operator2
    global op2_mode

    
    if op2_mode==False:
        operator1= float(numberScreen.get())

    if operation=="addition":
        addition()
    elif operation=="substraction":
        substraction()
    elif operation=="multiplication":
        multiplication()
    elif operation=="division":
        division()
    
    elif operator1!='' and operator2!='':
        result= operator1 ** float(operator2)
        numberScreen.set(result)
        operator1= result
        operator2= ''
        
    operation= "power_of"

    counter= 0
    reset_screen= True
    op2_mode= True


#------------------------ result con = ----------------------------

def the_result():

    global result
    global reset_screen
    global operator1
    global operator2
    global operation
    global op2_mode


    if operation=="addition":
        addition()                 
        
    elif operation=="substraction": 
        substraction()

    elif operation=="multiplication":
        multiplication()

    elif operation=="division":
        division()
        
    else:
        power_of()


    result=0
    reset_screen= True
    operation=""
    operator1=""
    operator2=""
    op2_mode= False
    



#-------------------------------------------------------
#-------------------------------------------------------





#--------------------screen---------------------------

numberScreen= StringVar()
numberScreen.set("0")

reset_screen= False

operation=""
result=""

operator1=""
operator2=""
op2_mode= False

screen= Entry(frame, textvariable= numberScreen)
screen.grid(row=0, columnspan=4, padx=10, pady=10)
screen.config(bg="black", fg="#03f943", justify="right")


#--------------------------1º fila--------------------

deleteKey= Button(frame, text="C", height=2, width=4, command= lambda:deleteEverything())
deleteKey.grid(row=1, column=0)

power_ofKey= Button(frame, text="X^y", height=2, width=4, command= lambda:power_of())
power_ofKey.grid(row=1, column=1)

delKey= Button(frame, text="Del", height=2, width=4, command= lambda:undo())
delKey.grid(row=1, column=2)

multiplicationKey= Button(frame, text="*", height=2, width=4, command= lambda: multiplication())
multiplicationKey.grid(row=1, column=3)


#--------------------------2º fila--------------------

number1= Button(frame, text="1", height=2, width=4, command= lambda:pressNumbers("1"))
number1.grid(row=2, column=0, pady=5)

number2= Button(frame, text="2", height=2, width=4, command= lambda:pressNumbers("2"))
number2.grid(row=2, column=1, pady=5)

number3= Button(frame, text="3", height=2, width=4, command= lambda:pressNumbers("3"))
number3.grid(row=2, column=2, pady=5)

teclaaddition= Button(frame, text="+", height=2, width=4, command= lambda:addition())
teclaaddition.grid(row=2, column=3, pady=5)


#--------------------------3º fila--------------------

number4= Button(frame, text="4", height=2, width=4, command= lambda:pressNumbers("4"))
number4.grid(row=3, column=0)

number5= Button(frame, text="5", height=2, width=4, command= lambda:pressNumbers("5"))
number5.grid(row=3, column=1)

number6= Button(frame, text="6", height=2, width=4, command= lambda:pressNumbers("6"))
number6.grid(row=3, column=2)

substractionKey= Button(frame, text="-", height=2, width=4, command= lambda: substraction())
substractionKey.grid(row=3, column=3)


#--------------------------4º fila--------------------

number7= Button(frame, text="7", height=2, width=4, command= lambda:pressNumbers("7"))
number7.grid(row=4, column=0, pady=5)

number8= Button(frame, text="8", height=2, width=4, command= lambda:pressNumbers("8"))
number8.grid(row=4, column=1, pady=5)

number9= Button(frame, text="9", height=2, width=4, command= lambda:pressNumbers("9"))
number9.grid(row=4, column=2, pady=5)

divisionKey= Button(frame, text="/", height=2, width=4, command= lambda: division())
divisionKey.grid(row=4, column=3, pady=5)


#--------------------------5º fila--------------------

number0= Button(frame, text="0", height=2, width=4, command= lambda:pressNumbers("0"))
number0.grid(row=5, column=1)

commaKey= Button(frame, text=",", height=2, width=4, command= lambda: pressComma())
commaKey.grid(row=5, column=2)

equal_toKey= Button(frame, text="=", height=2, width=4, command= lambda:the_result())
equal_toKey.grid(row=5, column=3)


#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


root.mainloop()