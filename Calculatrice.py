from tkinter import *
# Voici la fonction qui permet d'enregistrer les nombres selectionner dans les boutons du Calculator
def btnClick(numbers):
   global operator
   operator=operator +str(numbers)
   text_Input.set(operator)
# fin du fonction
# fonction pour effacer l'ecran du calculatrice
def btnClearDisplay():
   global operator
   operator=""
   text_Input.set("")
# fin du fonction
# fonction pour faire les calcules avec le bouton egale
def btnEqualsInput():
   global operator
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=""
cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=30,insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)
#Voila les codes pour afficher les bouton:"1,2...9,+,-,*,/,=,C(clear)"
##############################################################################################################################################
btn1=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)
btn2=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)
btn3=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)
AdditionButton=Button(cal,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
##############################################################################################################################################
btn4=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=2)
SubsButton=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
##############################################################################################################################################
btn7=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=0)
btn8=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)
btn9=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=2)
Multuplication=Button(cal,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="x",bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)
##############################################################################################################################################
btn9=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)
ButtomClear=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="C",bg="powder blue",command= btnClearDisplay).grid(row=4,column=1)
ButtonEquals=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="=",bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)
Division=Button(cal,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'), text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)
##############################################################################################################################################
cal.mainloop()



















