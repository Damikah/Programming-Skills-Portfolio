# -*- coding: utf-8 -*-
"""
Exercise 3: Biography - 25 Marks
"""
information={'first_name': str(input("Enter your first name:")),
             'last name': str(input("Enter your last name:")),
             'hometown': str(input("Enter your hometown:")),
             'age': str(input("Enter your age:"))}

"""
this code asks for the users input and stores the information that 
is inputted by the user as key-value pairs in a dictionary
"""
print("\nYour Information:")
for value in information.values(): 
    print(value)#selects and prints the values
    
"""
Advanced Requirement
"""
print("n\Your name is"+""+information['first_name']+""
      +information['last_name']+".")
#prints your name is 'first_name' 'last_name'.
print("Your hometown is in"+""+information['hometown']
      +".")
#prints your hometown is in ___.
print ("You are"+""+information['age']+""+"years old.")
#prints you are ___ years old.
