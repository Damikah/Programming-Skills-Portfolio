"""
Created on Fri Jan 10 00:32:00 2025

@author: Damikah Sierra
"""
import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Damikah Sierra/Desktop/Vending Machine/Bats Music.mp3')
pygame.mixer.music.play(loops=-1)


items = {
    'A1':{'Name': "Pepsi",'Cost': 5,'Stock': 10},
    'A2':{'Name': "Coca Cola",'Cost': 5,'Stock': 10},
    'A3':{'Name':"Mirinda",'Cost': 5,'Stock': 10},
    'A4':{'Name':"Mountain Dew",'Cost': 5,'Stock': 10},
    'A5':{'Name':"Sprite",'Cost': 5,'Stock': 10},
    'A6':{'Name': "Lipton Iced Tea",'Cost': 3,'Stock': 10},
    'B1':{"Name": "Hot Chocolate",'Cost': 10,'Stock': 10},
    'B2':{"Name": "Nescafe Coffee White",'Cost': 5,'Stock': 10},
    'B3':{"Name":"Nescafe Coffee Black",'Cost': 5,'Stock': 10},
    'B4':{"Name":"Nescafe Cappucino",'Cost': 5,'Stock': 10},
    'B5':{"Name":"Nescafe Mocha",'Cost': 5,'Stock': 10},
    'B6':{"Name": "Nescafe Original",'Cost': 5,'Stock': 10},
    'C1':{"Name": "Cheetos",'Cost': 3,'Stock': 10},
    'C2':{"Name": "Doritos",'Cost': 3,'Stock': 10},
    'C3':{"Name":"Lays",'Cost': 3,'Stock': 10},
    'C4':{"Name":"M&M's Chocolate",'Cost': 10,'Stock': 10},
    'C5':{"Name":"Maltesers",'Cost': 7,'Stock': 10},
    'C6':{"Name": "Kitkat",'Cost': 4,'Stock': 10}} 

Organized_List = ['Cold_Drinks', 'Hot_Drinks', 'Chips_and_Snacks']

Cold_Drinks = {
    'A1':{'Name': "Pepsi",'Cost': 5,'Stock': 10},
    'A2':{'Name': "Coca Cola",'Cost': 5,'Stock': 10},
    'A3':{'Name':"Mirinda",'Cost': 5,'Stock': 10},
    'A4':{'Name':"Mountain Dew",'Cost': 5,'Stock': 10},
    'A5':{'Name':"Sprite",'Cost': 5,'Stock': 10},
    'A6':{'Name': "Lipton Iced Tea",'Cost': 3,'Stock': 10}}
Hot_Drinks = {
    'B1':{"Name": "Hot Chocolate",'Cost': 10,'Stock': 10},
    'B2':{"Name": "Nescafe Coffee White",'Cost': 5,'Stock': 10},
    'B3':{"Name":"Nescafe Coffee Black",'Cost': 5,'Stock': 10},
    'B4':{"Name":"Nescafe Cappucino",'Cost': 5,'Stock': 10},
    'B5':{"Name":"Nescafe Mocha",'Cost': 5,'Stock': 10},
    'B6':{"Name": "Nescafe Original",'Cost': 5,'Stock': 10}}
Chips_and_Snacks = {
   'C1':{"Name": "Cheetos",'Cost': 3,'Stock': 10},
   'C2':{"Name": "Doritos",'Cost': 3,'Stock': 10},
   'C3':{"Name":"Lays",'Cost': 3,'Stock': 10},
   'C4':{"Name":"M&M's Chocolate",'Cost': 10,'Stock': 10},
   'C5':{"Name":"Maltesers",'Cost': 7,'Stock': 10},
   'C6':{"Name": "Kitkat",'Cost': 4,'Stock': 10}} 

print("------- Dami's Vending Machine -------\n\n")
print("---------- Menu Items Data ----------\n\n")

for key, item in items.items():
    print(f"{key}) {item['Name']} -- {item['Cost']} -- {item['Stock']}")
    
print("-----Would you like to sort the choices?-----")
Organized=str(input("-----yes or no-----"))
if Organized=="yes":
    print("Choose which list you want to sort")
    print(Organized_List, sep = ' / ')
    Chosen_Org= str(input("\nEnter chosen list here: "))
    if Chosen_Org == "Cold_Drinks":
     for key, item in Cold_Drinks.items():
        print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
        
    elif Chosen_Org == "Hot_Drinks":
     for key, item in Hot_Drinks.items():
        print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
        
    elif Chosen_Org == "Chips_and_Snacks":
     for key, item in Chips_and_Snacks.items():
        print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
    else:
        print("Invalid request")
product = input("Plase enter the item number you would like to purchase: ")

if product in items:
    selected_item = items[product]
    print("----------------------------------------")
    print(f"You have chosen {selected_item['Name']}.")
    print("----------------------------------------")
    amount_due = selected_item['Cost']

while amount_due > 0:
        try:
            payment = float(input(f"Please insert {amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print("----------------------------------------")
                print(f"You have successfully purchased {selected_item['Name']}!")
                print("----------------------------------------")
                print(f"Thank you for your purchase! Your change is {change:.2f}")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")