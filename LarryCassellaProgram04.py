#-----------------------------------------------------------------------------
#Author: Larry Cassella

#Program: Program 04

#Description: This program that will accept billing information for more than
#one employee and produce an invoice displaying all relevant information.
#-----------------------------------------------------------------------------

import Module4

def main():

    #Named constant for determining if employee worked ovetime
    overtime_threshold = 160

    #Named constant for overtime multiplier
    overtime_multiplier = 0.05

    #Variable to control the loop 
    keep_going = 'y'

    #Get employee name, hourly rate, and how many hours worked per week from user
    #and produces an invoice for any number of employees.
    while keep_going == 'y' or keep_going == 'Y':

        #Call readEmployeeName 
        employee_name = Module4.readEmployeeName("Employee Name: ")

        #Call readHourlyRate 
        hourly_rate = Module4.readHourlyRate("Hourly Rate: ")

        #Call readWeeklyHours
        week_one = Module4.readWeeklyHours("Enter hours worked for week 1: ")
        week_two = Module4.readWeeklyHours("Enter hours worked for week 2: ")
        week_three = Module4.readWeeklyHours("Enter hours worked for week 3: ")
        week_four = Module4.readWeeklyHours("Enter hours worked for week 4: ")

        #Calculate the total amount of hours work for the month
        total_hours = float(week_one + week_two + week_three + week_four)

        #Calculate the average total hours for a week 
        average_hours = float(total_hours/4)

        #Prints invoice for employee (includes overtime if applicable)
        if total_hours > overtime_threshold:
            overtime_hours = total_hours - overtime_threshold
            overtime_rate = (hourly_rate * overtime_multiplier) + hourly_rate 
            overtime_pay = overtime_hours * overtime_rate
            regular_hours = total_hours - overtime_hours
            regular_pay = regular_hours * hourly_rate
            amount_due = overtime_pay + regular_pay 
            print('\n' + employee_name, "worked", overtime_hours, "hours of overtime.")
            print('\nInvoice')
            print('Resource: ', employee_name, '\tAverage weekly hours: ',
                format(average_hours, '.2f'), sep ='')
            print('\nTotal billable hours: ', format(total_hours, '.2f'),
                '\tRate: $', format(hourly_rate, ',.2f'), sep = '')
            print("Overtime hours: ", format(overtime_hours, '.2f'), " @ $",
                format(overtime_rate, ',.2f'), "\t= $",
                format(overtime_pay, ',.2f'), sep = '')
            print("Regular hours: ", format(regular_hours, '.2f'), " @ $",
                format(hourly_rate, ',.2f'), "\t= $",
                format(regular_pay, ',.2f'), sep = '')
            print("Amount due: $", format(amount_due, ',.2f'), sep = '')
        else:
            amount_due = total_hours * hourly_rate
            print('\n' + employee_name, "worked no overtime.")
            print('\nInvoice')
            print('Resource: ', employee_name, '\tAverage weekly hours: ',
                format(average_hours, '.2f'), sep = '')
            print('\nTotal billable hours: ', format(total_hours, '.2f'),
                '\tRate: $', format(hourly_rate, ',.2f'), sep = '')
            print("Regular hours: ", format(total_hours, '.2f'), " @ $",
                format(hourly_rate, ',.2f'), "\t= $",
                format(amount_due, ',.2f'), sep = '')
            print("Amount due: $", format(amount_due, ',.2f'), sep = '')

        #See if the user wants to generate another invoice for different employee
        keep_going = str(input('\nEnter another employee? ("y" = yes): '))

    #Informs user that program ended normally
    print("\nProgram ended normally.")


main()
