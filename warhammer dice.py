import random

def roll_and_count(num_dice, dice_sides, threshold):
    rolls = [random.randint(1, dice_sides) for _ in range(num_dice)] #"for _ in range" ne pravi index vec samo govori pythonu da nas boli kurac za brojac, svaki throw broji posebno!
    hits = [roll for roll in rolls if roll > threshold] #pravi novi niz "roll" gde kaze da je roll deo od rolls samo ako je veci od uslova(threshold)
    return rolls, len(hits) #len hits je samo za broj hitova koji su prosli

#ne zam koliko je ovo stabilno!
# x je broj kocika a y broj strana, !!!DEFINISANO U LINIJI 26!!!
units = {
        "1": (6, 6), #swords
        "2": (8, 6), #greatswords
        "3": (14, 6) #knights
    }
print("avalible units:")
print("1. swords men")
print("2. greatswords men")
print("3.reiksguard knights")

while True:
    unit = input("With what unit should you attack?").strip() #strip just dont care for the spaces
        

    if unit in units:
        num_dice, dice_sides = units[unit]
        rolls, passed = roll_and_count(num_dice, dice_sides, threshold=3)
        print(f"Rolls: {rolls}")
        print(f"{passed} of them went through!")
        break
    else:
        print("please chose one of the units above!.")