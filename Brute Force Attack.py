# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack - 30 Marks
"""
password= "12345"#password variable
guesses= ""#the variable for guesses
attempts= 5#number of attempts 

while attempts>0:#if attempts>0, user can keep guessing
    guess= input("Enter the password: ")#user inputs guesses here
    if guess== password:
        print("Correct Password!")#prints if guess is correct
        break#end of code if answer is correct
    else:
        attempts= attempts - 1 #number of attempts lessen by 1 if answer is wrong
        print("Incorrect Password, you have", attempts,"attempts remaining")
        #prints if password incorrect, says number of attempts left
        if attempts == 0:
            print("You have made too many attempts, the authorities have been alerted.")
            #prints if password is wrong and number of attempts are 0 
