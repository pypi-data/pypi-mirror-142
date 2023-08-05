from poker_chances import chances
from tkinter import *
player_hand = []
enemy_count = []

def click():
    global entered_text
    global h
    #entered_text = textentry.get()
    print(entered_text)
    #print(type(h))
    h.table_cards(entered_text)
    #output.delete(0.0, END)
    #output.insert(END, entered_text)
    
def click2():
    global entered_text
    entered_text = textentry.get()
    entered_text = entered_text + "_spades"
    output.delete(0.0, END)
    output.insert(END, entered_text)

def click3():
    global entered_text
    entered_text = textentry.get()
    entered_text = entered_text + "_clubs"
    output.delete(0.0, END)
    output.insert(END, entered_text)

def click4():
    global entered_text
    entered_text = textentry.get()
    entered_text = entered_text + "_diamonds"
    output.delete(0.0, END)
    output.insert(END, entered_text)

def click5():
    global entered_text
    entered_text = textentry.get()
    entered_text = entered_text + "_hearts"
    output.delete(0.0, END)
    output.insert(END, entered_text)

def click6():
    global h
    h.end_round()

def click7():
    global entered_text
    #entered_text = textentry.get()
    player_hand.append(entered_text)
    print(player_hand)

def click8():
    global h
    h = chances(enemy_count[0],player_hand[0], player_hand[1])

def click9():
    entered_text2 = enemy_fold_output.get()
    h.enemy_fold(int(entered_text2))


def click10():
    entered_text3 = enemy_amount.get()
    enemy_count.append(int(entered_text3))

    
    
window = Tk()
window.title("poker_chances")

Label(window, text="first press what type of cards it is, so A or K and so on.", bg="white", fg="black", font="none 10 bold") .grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="table_card", width=20, command=click) .grid(row=3, column=0, sticky=W)
Button(window, text="initiate", width=20, command=click8) .grid(row=2, column=1, sticky=W)
Button(window, text="spades", width=20, command=click2) .grid(row=4, column=1, sticky=W)
Button(window, text="clubs", width=20, command=click3) .grid(row=5, column=1, sticky=W)
Button(window, text="diamonds", width=20, command=click4) .grid(row=6, column=1, sticky=W)
Button(window, text="hearts", width=20, command=click5) .grid(row=7, column=1, sticky=W)
Button(window, text="starting_cards", width=20, command=click7) .grid(row=8, column=1, sticky=W)
Button(window, text="end_round", width=20, command=click6) .grid(row=9, column=1, sticky=W)
Button(window, text="enemy_fold", width=20, command=click9) .grid(row=7, column=0, sticky=W)
Button(window, text="enemy_amount", width=20, command=lambda: click10) .grid(row=5, column=0, sticky=W)

enemy_amount = Entry(window, width=20,bg="white")
enemy_amount.grid(row=4, column=0, sticky=W)

enemy_fold_output = Entry(window, width=20,bg="white")
enemy_fold_output.grid(row=6, column=0, sticky=W)

output = Text(window, width=25, heigh=4, wrap=WORD, bg="white")
output.grid(row=9,column=0,columnspan=2, sticky=W)


print(__name__)
window.mainloop()
