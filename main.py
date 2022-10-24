import urllib.request
import os
import random
import json
import ctypes
import time
import os
import pickle
import random
import sys
gold = 0

# Update
rareegg = random.randint(1,3)
rareegggift = True
pethealth = 100
ver = 1.0
menuselector = ''
# Player stats
playerclass = ''
health = 100
armor = 'none'
level = 1
maplevel = 1
name = 'John'
equipedweapon = ''
damage = 0
equipedarmor = ''
equipedpets = 'none'
choosename = name
playerclasschoose = playerclass
# End Player Stats
# Define Statements
def Begin():
  global choosename
  global playerclasschoose
  global playerclass
  global equipedweapon
  print("Hey there!")
  print("Before we begin, you need to choose a class and name. Lets do that now!")
  print()
  choosename = input("What is your roleplay name? ")
  print("That is amazing!")
  print("You are now ready to begin!")
  choosename = name
  playerclasschoose = input("What is your class? (M) Mage (F) Figher (E) Medic")
  if playerclasschoose == 'M':
    playerclass = 'Mage'
    equipedweapon = 'Starter Magic Book'
    Save()
    clear_console()
    Menu()
  if playerclasschoose == 'F':
    playerclass = 'Figher'
    equipedweapon == 'Wooden Sword'
    Save()
    clear_console()
    Menu()
  if playerclasschoose == 'E':
    playerclass = 'Medic'
    equipedweapon == 'Sore Denier'
def clear_console():
  time.sleep(0.1)  
  os.system('clear')
def slowclear_console():
  time.sleep(10)  
  os.system('clear')
def slow_console():
  time.sleep(3)  
  os.system('clear')
def slower_console():
  time.sleep(2)  
  os.system('clear')
def loading():
  print('.')
  slower_console()
  print("..")
  slower_console()
  print("...")
  slower_console()
def Save():
  Save = str(playerclass) + str(health) + str(armor) + str(level) + str(maplevel) + str(name) + str(equipedweapon) + str(damage) + str(equipedweapon) + str(damage) + str(equipedarmor) + str(equipedpets) + str(rareegggift) + str(gold)
  pickle.dump(Save, open("savedata", "wb"))
def Load():
  pickle.load(open("savedata","rb")) 
def Menu():
  print("                    ===Menu===")
  print()
  print("(L) Level Selection")
  print()
  print("(C) Customization, Weaponry")
  print()
  print("(S) Stats")
  print()
  print("(A) Save")
  print()
  print("(X) Shop")
  print()
  print()
  global menuselector
  menuselector = input("Please type the selected letter and press enter ")
def levelsel():
  Save()
  clear_console()
  print("")
  print("Levels are still in beta. please be carefull when using.")
  print()
  print("(1) Level One")
  print()
  print("(2) Level Two")
  print()
  print("(M) Menu")
  print()
  print("(H) Halloween Town (TESTING)")
  global levelin 
  levelin = input("Please type the selected letter.")

# End define statements
# Start new player asker (I DONT KNOW WHAT TO CALL IT XD)
import requests
r = requests.get('https://update.samr9002.repl.co/updateavalible.py')
if r.status_code == 200:
    newversion = input("An Update is avalible! We recommend going to our site and downloading to the most recent version.")
    slow_console()
Load()
Menu()
# End new player asker
if menuselector == 'X':
  clear_console()
  print("                    SHOP")
  print("                  GOLD: " + str(gold))
  print("")
  print()
  print("WIP")
  print()
  menubackshop = input("type back to return to menu.")
  if menubackshop == 'back':
    clear_console()
    Save()
    Menu()
if menuselector == 'L':
  levelsel()
  Save()
  if levelin == 'H':
    clear_console()
    print("Welcome to halloween town!")
    slow_console()
    Menu()
  if levelin == 'M':
    Save()
    clear_console()
    Menu()
  if levelin == '1':
    clear_console()
    print("BLAH")
    Save()
  if levelin == '2':
    clear_console()
    print("BLAH")
    Save()
if menuselector == 'A':
  clear_console()
  Save()
  Load()
  print("Saved")
  slow_console()
  Menu()
if menuselector == 'S':
  clear_console()
  print("                    Stats")
  print()
  print("Health: " + str(health))
  print()
  print("ARMOR SET: " + str(armor))
  print()
  print("LEVEL: " + str(level))
  print()
  print("GOLD: " + gold)
  print()
  menuback = input("Type back to return to menu, and then press enter.")
  if menuback == 'back':
    clear_console()
    Save()
    Menu()
if menuselector == 'C':
  Save()
  clear_console()
  print("                Customization")
  print()
  print("(W) Weapons")
  print()
  print("(A) Armor")
  print()
  print("(P) Pets")
  print()
  print("(N) Name Changer  (FREE)")
  print()
  print("(M) Menu")
  print()
  print("(C) Class")
  print()
  print()
  custom = input("Type the selected letter and press enter.")
  if custom == 'M':
    Save()
    Menu()
  if custom == 'N':
    newname = input("Please type your new name...")
    name = newname
    Save()
    Menu()
    # Classes
  if custom == 'C':
    clear_console()
    print("                   CLASSES")
    print()
    print("(M) Mage")
    print()
    print("(F) Fighter")
    print()
    print("(E) Medic")
    print()
    print("More coming in a later version...")
    print()
    print()
    classselection = input("Type the selected letter, then press enter.")
    if classselection == 'M':
      clear_console()
      print("Mage Selected")
      playerclass = 'Mage'
      Save()
      clear_console()
      Menu()
    if classselection == 'F':
      clear_console()
      print("Figher Selected")
      playerclass = 'Fighter'
      Save()
      clear_console()
      Menu()
    if classselection == 'E':
      clear_console()
      print("Medic Selected")
      playerclass = 'Medic'
      Save()
      clear_console()
      Menu()
    # Classes
  if custom == 'W':
    clear_console()
    print("                WEAPONS")
    if playerclass == 'Mage':
      print("Current Magic Book Equiped: " + equipedweapon)
    if playerclass == 'Fighter':
      print("Current Sword Equiped: " + equipedweapon)
    if playerclass == 'Medic':
      print("Current Sore Denier Equiped: " + equipedweapon)
    if playerclass == '':
      print("You are not a mage or fighter or medic. Go select your class!")
      slowclear_console()
      Menu()
      print("")
      print()
    # armor
  if custom == 'A':
    clear_console()
    print("                    ARMOR")
    if equipedarmor == '':
      print("Current Armor Equiped: none")
      print()
      print("(L) Leather Armor")
      print("")
      print("(B) Back To Menu")
      print()
      armornow = ("Type the letter wanted, and press enter.")
      if armornow == 'B':
        Menu()
      if armornow == 'L':
        leatherequip = input("Equip? Y or N.")
        if leatherequip == 'N':
          clear_console()
          print()
          clear_console()
          Menu()
      if leatherequip == 'Y':
        clear_console()
        print("You equiped the armor: Leather Armor")
        equipedarmor = 'Leather Armor'
        clear_console()
        Menu()
    else:
      print("Current Armor Equiped: " + equipedarmor)
      print()
      print("(L) Leather Armor")
      print("")
      print()
      armornow = ("Type the letter wanted, and press enter.")
      if armornow == 'L':
        leatherequip = input("Equip? Y or N.")
        if leatherequip == 'N':
          clear_console()
          print()
          clear_console()
          Menu()
      if leatherequip == 'Y':
        clear_console()
        print("You equiped the armor: Leather Armor")
        equipedarmor = 'Leather Armor'
        clear_console()
        Menu()
    # armor
    # PETS
  if custom == 'P':
    clear_console()
    if rareegggift == False:
      clear_console()
      print("                     PETS")
      print("              Current pet: " + str(equipedpets))
      print()
      print("Pets Avalible:")
      print()
      print(str(equipedpets))
      print()
      windows = input("Please type the selected letter.")
      clear_console()
    if rareegggift == True:
       print("                     PETS")
       print("              Current pet: " + str(equipedpets))
       print()
       print("Pets Avalible:")
       print()
       print("(R) Rare Egg (Gift from admins)")
       print()
       windows = input("Please type the selected letter.")
       clear_console()
       if windows == 'R':
        print("Rare Egg")
        print()
        print("Health: ???")
        print("Damage: ???")
        print("Class: ???")
        print()
       hatch1 = input("Hatch this egg? Y or N.")
       if hatch1 == 'N':
         Menu()
         Save()
       if hatch1 == 'Y':
         rareegggift = False
         Save()
       if rareegg == 1:
           clear_console()
           equipedpets = '(S) Fiery Dragon'
           ep = 'FD'
           print("Fiery Dragon")
           Save()
           clear_console()
           Menu()
       if rareegg == 2: 
          clear_console()
          equipedpets = '(E) Elemental Dragon'
          ep = 'ED'
          print("Elemental Dragon")
          Save()
          Menu()
          clear_console()
       if rareegg == 3:
          clear_console()
          equipedpets = '(FD) Fire Dragon'
          ep = 'FID'
          print("Fire Dragon")
          Save()
          Menu()
          clear_console()
       if windows == 'FD':
         clear_console()
         print("                   Fire Dragon")
         print()
         print("HEALTH: " + pethealth)
    # PETS