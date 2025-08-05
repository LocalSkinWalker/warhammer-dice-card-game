import random
import tkinter as tk
from tkinter import *
import pygame  # sound playback

# Initialize mixer
pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("sound.wav")  # or .mp3
    pygame.mixer.music.play()

def roll_and_count(num_dice, dice_sides, threshold):
    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]
    hits = [roll for roll in rolls if roll > threshold]
    return rolls, len(hits)

units = {
    "Swordsmen": (6, 6),
    "Greatswords": (8, 6),
    "Reiksguard Knights": (14, 6)
}

def on_unit_click(unit_name):
    play_sound()  # Play sound when unit button is clicked
    num_dice, dice_sides = units[unit_name]
    rolls, passed = roll_and_count(num_dice, dice_sides, threshold=3)
    result_text.set(f"Unit: {unit_name}\nRolls: {rolls}\n{passed} of them went through!")

window = tk.Tk()
window.title("Warhammer The Old World")
window.geometry("600x500")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

icons = {
    "Swordsmen": PhotoImage(file='swordsmen icon.png'),
    "Greatswords": PhotoImage(file='greatswords icon.png'),
    "Reiksguard Knights": PhotoImage(file='reiksguard knights icon.png')
}

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=10)  # Fixed from pack=10 to pady=10

for unit_name in units:
    dugme = tk.Button(window,
                      text=unit_name,
                      font=("Castellar", 16),
                      image=icons[unit_name],
                      width=180,
                      height=320,
                      compound="top",
                      command=lambda u=unit_name: on_unit_click(u))
    dugme.pack(side="left", padx=10)

window.mainloop()