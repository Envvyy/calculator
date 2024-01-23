import tkinter as tk
from math import *

BUTTON_WEITH = 4
BUTTON_HEIGHT = 2

firstInput = ''
signInput = ''
secondInput = ''

window = tk.Tk()
window.title("Калькулятор")
window.geometry('314x478')
buttonFont = ("Helvetica", 22)
printt = tk.Label(width = 44, justify="right")

def updateTextNumber(num):
    def F():
        newText = printt.cget("text") + str(num) 
        printt.config(text=newText)
    return F

def commaInText():
    if '.' in printt.cget("text"):
        return
    else:
        newText = printt.cget("text") + '.'
        printt.config(text=newText)

def updateTextSign(signn):
    def D():
        global firstInput
        firstInput = printt.cget("text")
        global signInput
        signInput = signn
        printt.config(text = '')
    return D

def createButton(row,column,command,text):
    newButton = tk.Button(text=text, width = BUTTON_WEITH, height = BUTTON_HEIGHT,bg = 'snow4',font = buttonFont,command = command)
    newButton.grid(row = row,column = column)
    return newButton

def eraseNumber():
    global printt
    printt.config(text = str(printt.cget("text"))[:-1])

def signNumber():
    global printt
    printt.config(text = '-' + str(printt.cget("text")))
    
def equalsResult():
    global secondInput
    secondInput = printt.cget('text')
    match signInput:
        case "+":
            return printt.config(text = str(float(firstInput) + float(secondInput)))
        case "-":
            return printt.config(text = str(float(firstInput) - float(secondInput)))
        case "x":
            return printt.config(text = str(float(firstInput) * float(secondInput)))
        case ":":
            return printt.config(text = str(float(firstInput) / float(secondInput)))
        case "^":
            return printt.config(text = str(float(firstInput) ** (float(secondInput))))
        case "sqrt":
            return printt.config(text = str((float(firstInput)**(1/float(secondInput)))))

one = createButton(4,0,updateTextNumber(1),'1')
two = createButton(4,1,updateTextNumber(2),'2')
three = createButton(4,2,updateTextNumber(3),'3')
four = createButton(3,0,updateTextNumber(4),'4')
five = createButton(3,1,updateTextNumber(5),'5')
six = createButton(3,2,updateTextNumber(6),'6')
seven = createButton(2,0,updateTextNumber(7),'7')
eight = createButton(2,1,updateTextNumber(8),'8')
nine = createButton(2,2,updateTextNumber(9),'9')
null = createButton(5,1,updateTextNumber(0),'0')
sign = createButton(5,0,signNumber,'+/-')
plus = createButton(4,3,updateTextSign('+'),'+')
minus = createButton(3,3,updateTextSign('-'),'-')
multiplication = createButton(2,3,updateTextSign('x'),'x')
division = createButton(1,2,updateTextSign(':'),':')
degree = createButton(1,1,updateTextSign('^'),'^')
erase = createButton(1,3,eraseNumber,'<=')
root = createButton(1,0,updateTextSign('sqrt'),'sqrt')
comma = createButton(5,2,commaInText,'.')
equals = createButton(5,3,equalsResult,'=')

printt.grid(row = 0, column = 0, columnspan = 4)

window.mainloop()