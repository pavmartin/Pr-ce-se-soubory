# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:36:57 2019

@author: Martin
"""

def prevod():
    try:
        vstJmeno = input("Zadej jméno vstupního souboru: ")
        vstSoubor = open(vstJmeno, "r")
        vystJmeno = input("Zadej jméno výstupního souboru: ")
        vystSoubor = open(vystJmeno,"w")
        while True:
            radek = vstSoubor.readline()
            if radek == '':
                break
            vystSoubor.write(radek.upper())
            vystSoubor.write(radek.lower())
        vstSoubor.close()
        vystSoubor.close()
        print("\nHotovo\n")
    except IOError:
        print("\nŠpatná cesta k souboru")

def nahrad():
    try:
        vstJmeno = input("Zadej jméno vstupního souboru: ")
        vstSoubor = open(vstJmeno, "r")
        vystJmeno = input("Zadej jméno výstupního souboru: ")
        vystSoubor = open(vystJmeno,"w")
        znakStary = input("Zadej znak, který se má nahradit: ")
        znakNovy = input("Zadej znak, kterým se má starý znak nahradit: ")
        while True:
            radek = vstSoubor.readline()
            if radek == '':
                break
            vystSoubor.write(radek.replace(znakStary,znakNovy))
        vstSoubor.close()
        vystSoubor.close()
        print("\nHotovo\n")
    except IOError:
        print("\nŠpatná cesta k souboru")
        
while True:
    print("1. Převod na malá písmena")
    print("2. Nahrazení znaků")
    print("3. Konec")
    try:
        volba = int(input("1-3> "))
        if volba == 1:
            prevod()
        elif volba == 2: 
            nahrad()
        elif volba == 3: 
            exit = 0
        else:
            print("\n>>>> Zadej číslo od 1 do 3\n")
    except ValueError: 
        print("\n>>>> Zadej číslo od 1 do 3\n")
    except EOFError: 
        exit = 0