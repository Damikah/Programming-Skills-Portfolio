# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month - 30 Marks
"""
Months_and_Days={1:31,
                 2:28,
                 3:31,
                 4:30,
                 5:31,
                 6:30,
                 7:31,
                 8:31,
                 9:30,
                 10:31,
                 11:30,
                 12:31}
#created a dictionary of the months and days
your_year=int(input("Enter the year number:"))#created a variable for the user input(year)
month_number=int(input("Enter the month number:"))#ceated a variable for the user inpit(month)

def leap(year): 
    if(year % 400 ==0) or (year % 4==0 and year %100 != 0): 
        return True
    return False
if leap(your_year):#checks for a leap year
    print("This is a leap year")
    if month_number not in Months_and_Days:
        print("Invalid month number")#prints this message if not included in the dictionary
    else:
        if month_number ==2:
            print("There are",Months_and_Days[month_number]+1,"days in this month.")
        else:
            print("There are", Months_and_Days[month_number], "days in this month.")
else:#if not a leap year
            print("This is not a leap year")
            if month_number not in Months_and_Days:
                print("Invalid month number")#not in dictionary
            else:#in dictionary
                print("There are",Months_and_Days[month_number], "days in this month.")


