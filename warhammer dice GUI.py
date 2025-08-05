import random
import tkinter as tk
from tkinter import * #iz nekog razloga ako izvucem photoimage samo nece raditi

def roll_and_count(num_dice, dice_sides, threshold):
    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)] #"for _ in range" ne pravi index vec samo govori pythonu da nas boli kurac za brojac, svaki throw broji posebno!
    hits = [roll for roll in rolls if roll > threshold] #pravi novi niz "roll" gde kaze da je roll deo od rolls samo ako je veci od uslova(threshold)
    return rolls, len(hits) #len hits je samo za broj hitova koji su prosli

units = {
    "Swordsmen": (6, 6), # x je broj kocika a y broj strana, !!!DEFINISANO U LINIJI 17!!!
    "Greatswords": (8, 6),
    "Reiksguard Knights": (14, 6)
}

def on_unit_click(unit_name):
    num_dice, dice_sides = units[unit_name]
    rolls, passed = roll_and_count(num_dice, dice_sides, threshold=3)
    result_text.set(f"Unit: {unit_name}\nRolls: {rolls}\n{passed} of them went through!")

#od ovde pocinje prozor
window = tk.Tk()
window.title("Warhammer The Old World")
window.geometry("600x500")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)

icons = {
    "Swordsmen":  PhotoImage(file='swordsmen icon.png'),
    "Greatswords": PhotoImage(file='greatswords icon.png'),
    "Reiksguard Knights": PhotoImage(file='reiksguard knights icon.png')
}

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text) 
result_label.pack(padx=10)

for unit_name in units:
    dugme = tk.Button(window,
                    text=unit_name,
                    font=("Castellar", 16),
                    image=icons[unit_name],
                    width=180,
                    height=320,
                    compound="top",
                    command=lambda u=unit_name: on_unit_click(u))
    dugme.pack(side ="left", padx=10)
window.mainloop()
