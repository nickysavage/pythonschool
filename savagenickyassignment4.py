'''
Nicky Savage
ENTD200 I002 Win 16
Sammy
Week  4 
Date completed; February 24th 2016
I learned this comment trick from
Guido van Rossum (creator of Python)

I added both assignments together, so it will run assignment one then run
assignment two.

Assignment one
Write a program to solve a simple payroll calculation.
Find the amount of pay given, hours worked, and hourly
rate. (The formula to calculate payroll is pay =
hourly rate * hours worked.) Use these values to test
the calculation: Problem 1A (hours = 30 and rate = 8.52)
and Problem 1B (hours = 53 and rate = 11.54). Display
hourly rate, hours worked, and pay. Use the print command
and make basic mathematical calculations.
'''
hourly_rate = float(input("Enter Hourly Rate :"))
hours_worked = float(input("Enter no of hours worked :"))
pay = hourly_rate*hours_worked

print ("Hourly Rate : " + str(hourly_rate))
print ("Hours worked : " + str(hours_worked))

if hours_worked > 40:
    pay = hourly_rate*40 + hourly_rate*1.5*(hours_worked-40)
else:
    pay = hourly_rate*hours_worked

print ("Hourly Rate : " + str(hourly_rate))
print ("Hours worked : " + str(hours_worked))
print ("pay : " + str(pay))

'''
Problem 2: Write a program that will calculate the average
miles per gallon obtained on a trip. Input the amount of gas
used and the number of miles driven. (The formula to calculate
miles per gallon is miles per gallon = number of miles driven
/ amount of gas used. ) Use these values to test the calculation:
Problem 2 (number of miles driven = 298) and (amount of gas used = 12.17).
Use the print command and make basic mathematical calculations.
'''

miles = float(input("Enter no of miles driven :"))
gas = float(input("Enter amount of gas :"))

mpg = miles/gas

print ("Miles Driven : " + str(miles))
print ("Gas : " + str(gas))
print ("Miles per gallon : " + str(mpg))



























