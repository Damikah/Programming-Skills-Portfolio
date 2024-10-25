# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search - 30 Marks
"""
my_list=["Jake","Zac","Ian","Ron","Sam","Dave"]#list of names
print("Objective: Find the person who stole the doughnut! You have one attempt!")
print(my_list)
search=str(input("Enter the name of the person who stole the doughnut: "))#asks for users input
if search== "Sam":
    print("Amazing!You did it!It was Sam!")#if user input/guess is correct(Sam)
else:
    print("Aw man, its not that dude")#if user input/guess is incorrect
