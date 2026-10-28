from tkinter import *

# --- état global ---
expression = ""   


AUTORISES = set("0123456789+-*/.")

def _expression_valide(expr):
    """Vérifie que l'expression ne contient que des caractères sûrs."""
    return expr != "" and all(c in AUTORISES for c in expr)

def btnClick(numbers):
    global expression
    # Bug 5 : éviter "05", "007", etc.
    if str(numbers) == "0" and (expression == "" or expression[-1] in "+-*/"):
        # on autorise "0" seul ou après un opérateur, mais pas "00"
        if expression.endswith("0"):
            return
    # Bug 4 : empêcher deux points dans le même nombre
    if str(numbers) == ".":
        dernier_nombre = expression.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()[-1] if expression else ""
        if "." in dernier_nombre:
            return
    expression = expression + str(numbers)
    text_Input.set(expression)

def btnClearDisplay():
    global expression
    expression = ""
    text_Input.set("")

def btnEqualsInput():
    global expression
    # Bugs 1, 2, 3 : validation + try/except + gestion de l'état après "="
    if not _expression_valide(expression):
        text_Input.set("Erreur")
        expression = ""
        return
    try:
        resultat = str(eval(expression))
    except ZeroDivisionError:
        resultat = "Division par 0"
    except Exception:
        resultat = "Erreur"
    text_Input.set(resultat)
    # Bug 3 : si le résultat est un nombre, on le garde pour enchaîner les calculs
    expression = resultat if resultat not in ("Erreur", "Division par 0") else ""

cal = Tk()
cal.title("Calculator")
cal.resizable(False, False)   # bonus : évite le redimensionnement bizarre

text_Input = StringVar()
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input,
                   bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)


def _btn(texte, ligne, colonne, commande):
    b = Button(cal, padx=16, pady=16, bd=8, fg="black",
               font=('arial', 20, 'bold'), text=texte, bg="powder blue",
               command=commande)
    b.grid(row=ligne, column=colonne)
    return b

btn7 = _btn("7", 1, 0, lambda: btnClick(7))
btn8 = _btn("8", 1, 1, lambda: btnClick(8))
btn9 = _btn("9", 1, 2, lambda: btnClick(9))
AdditionButton = _btn("+", 1, 3, lambda: btnClick("+"))

btn4 = _btn("6", 2, 0, lambda: btnClick(6))
btn5 = _btn("5", 2, 1, lambda: btnClick(5))
btn6 = _btn("4", 2, 2, lambda: btnClick(4))
SubsButton = _btn("-", 2, 3, lambda: btnClick("-"))

btn1 = _btn("3", 3, 0, lambda: btnClick(3))
btn2 = _btn("2", 3, 1, lambda: btnClick(2))
btn3 = _btn("1", 3, 2, lambda: btnClick(1))
Multuplication = _btn("x", 3, 3, lambda: btnClick("*"))

btn0 = _btn("0", 4, 0, lambda: btnClick(0))
# Bug 4 : ajout du point décimal (remplace une place libre)
PointButton = _btn(".", 4, 1, lambda: btnClick("."))
ButtomClear = _btn("C", 4, 2, btnClearDisplay)
ButtonEquals = _btn("=", 4, 3, btnEqualsInput)

Division = _btn("/", 5, 0, lambda: btnClick("/"))

cal.mainloop()
