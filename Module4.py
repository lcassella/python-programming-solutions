#-----------------------------------------------------------------------------
#Author: Larry Cassella
#File: Module4.py
#Program: Module 04
#Date Created: 3/24/2020
#-----------------------------------------------------------------------------

def readWeeklyHours(week):
    hours_worked = float(input(week))

    #Input validation for hours worked for one week 
    while hours_worked < 35 or hours_worked > 80:
        print("\nInvalid number of hours, must be between", 35, "and", 80, end = '.')
        hours_worked = float(input('\n\n' + week))
        
    return hours_worked

def readHourlyRate(rate):
    hourly_wage = float(input(rate))
    
    #Input validation for hourly rate
    while hourly_wage < 20:
        print("\nInvalid Hourly Rate, must be at least $", format(20, '.2f'), "/hour.", sep = '')
        hourly_wage = float(input('\n\n' + rate))

    return hourly_wage

def readEmployeeName(name):
    name_entered = input(name)

    #Input validation for employee name 
    while name_entered == '':
        print("\nEmployee Name must be entered.")
        name_entered = input("\n\nEmployee Name: ")

    return name_entered 
