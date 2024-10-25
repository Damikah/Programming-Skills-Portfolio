# -*- coding: utf-8 -*-
"""
Exercise 10: Is it even? - 35 Marks
"""
def even(number): #the function for even
    return number % 2==0#if number is divisible by 2 and remainder of 0
def odd(number):
    return number %2==1#if number is divisible by 2 and has a remainder of 1
def main():
    number= int(input("Enter a number: "))#asks for the user input(number)
    
    if even(number):#if the number inputted has a remainder of 0
        print("The number you have entered is even")
    elif odd(number):#if the number inputted has a remainder of 11
        print("The number you have entered is odd")
main()
