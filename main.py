from classes.parser import Parser
from classes.Tokens import Tokens
from classes.translator import Translator
from tkinter import *
from Input import Input

"""



print("traducción: " + result)"""

color1 = "gray81"
color2 = "gray76"


root = Tk()
root.geometry("500x200")
root.title("Traductor de ingles a español")
root.config(background=color1)


frame = Frame(width= 400 , height= 200,background=color2)

# LABEL INGRESE
label = Label(frame, text="Ingrese el texto: ", font='Tahoma 8 bold', background=color2 )
label.place(x=9, y=75)


label_typeText = Label(frame, text="", background=color2, font='Tahoma 12 bold')
label_typeText.place(x=10, y=140)

label_translation = Label(frame, text="", background=color2, font='Tahoma 13')
label_translation.place(x=10, y=170)

# LABEL TRADUCTOR
label = Label(frame, text="TRADUCTOR", font='Tahoma 8 bold', background=color2)
label.place(x=180, y=20)

# ENTRADA
input = Text(frame)
input.place(x=120, y=40)
input.config(width=25, height=5)

# BOTON Y ACCION


def translate():
    text = input.get(1.0, "end-1c")

    # TRADUCIR
    if text != "":
        parser = Parser('en')
        sentence = parser.parse_text(text)
        if sentence:
            sentence = sentence.replace('_', ' ')
            translator = Translator('en_es')
            result = translator.translate(Tokens.get())
            label_typeText.config(text=sentence)
            label_translation.config(text="Traducción: {}".format(result))
            Tokens.reset()
        else:
            label_translation.config(text="")
            label_typeText.config(text="Ha ocurrido un error en la sintaxis")


#BOTON TRADUCIR
btn_send = Button(frame, text="Traducir", font='Tahoma 10 bold')
btn_send.place(x=330, y=70)
btn_send.config(command=translate,borderwidth= 0)


frame.pack()
root.mainloop()
