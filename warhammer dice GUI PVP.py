import random 
import tkinter as tk

player1 = "Luka"
player2 = "Buzmiz"
player_dice = {player1: None, player2: None}
current_player = None

def roll_and_count(num_dice, dice_sides, threshold):
    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]  #"for _ in range" ne pravi index vec samo govori pythonu da nas boli kurac za brojac, svaki throw broji posebno!
    hits = [roll for roll in rolls if roll > threshold]  #pravi novi niz "roll" gde kaze da je roll deo od rolls samo ako je veci od uslova(threshold)
    return rolls, len(hits)  #len hits je samo za broj hitova koji su prosli

units = {
    "Swordsmen": (6, 6), #x je broj kocika a y broj strana, !!!DEFINISANO U LINIJI 33!!!
    "Greatswords": (8, 6),
    "Reiksguard \n Knights": (14, 6),
    "Norsca Warriors": (6, 6),
    "Chaos Warriors": (8, 6),
    "Chaos \n Knights": (14, 6)
}
#WRITEN BY AI! 19-23
def select_player(player):
    global current_player
    current_player = player
    result_text.set(f"{player} is selecting a unit.")

def on_unit_click(unit_name):
    global current_player

    if not current_player:
        result_text.set("Choose a player first!")
        return

    num_dice, dice_sides = units[unit_name]
    rolls, hits = roll_and_count(num_dice, dice_sides, threshold=3)
    
    player_dice[current_player] = hits

    result_text.set(f"{current_player} rolled {hits} hits for {unit_name}.\nRolls: {rolls}")

    if None not in player_dice.values():
        if player_dice[player1] > player_dice[player2]:
            winner = f"{player1} wins!"
        elif player_dice[player2] > player_dice[player1]:
            winner = f"{player2} wins!"
        else:
            winner = "It's a tie!"

        result_text.set(result_text.get() + f"\n{winner}")
        #sledece resetuje igru
        player_dice[player1] = None
        player_dice[player2] = None
        current_player = None
#od ovde pocinje prozor
window = tk.Tk()
window.title("Warhammer The Old World")
window.geometry("1280x720")

icon = tk.PhotoImage(file='icon.png')
window.iconphoto(True, icon)

icons = {
    "Swordsmen": tk.PhotoImage(file='swordsmen icon.png'),
    "Greatswords": tk.PhotoImage(file='greatswords icon.png'),
    "Reiksguard \n Knights": tk.PhotoImage(file='reiksguard knights icon.png'),
    "Norsca Warriors": tk.PhotoImage(file='norsca warrior icon.png'),
    "Chaos Warriors": tk.PhotoImage(file='chaos warriror icon.png'),
    "Chaos \n Knights": tk.PhotoImage(file='chaos knight icon.png')
}

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=10)
#dugmad za igrace
dugme_player1 = tk.Button(window,
                          text=player1,
                          font=("Castellar", 16),
                          command=lambda: select_player(player1))
dugme_player1.pack()

dugme_player2 = tk.Button(window,
                          text=player2,
                          font=("Castellar", 16),
                          command=lambda: select_player(player2))
dugme_player2.pack()
#dugmad za unite
for unit_name in units:
    dugme = tk.Button(window,
                      text=unit_name,
                      font=("Castellar", 16),
                      image=icons[unit_name],
                      width=180,
                      height=320,
                      compound="top",
                      command=lambda u=unit_name: on_unit_click(u))
    dugme.pack(side='left', expand=True, padx=10, pady=10)

window.mainloop()