# Author: Asif Ali Mehmuda
# Email: asif.mehmuda9@gmail.com
# This file exposes some of the common mathematical functions 

def add_nums(num1, num2):
    return num1 + num2

# Subtract two numbers 
def sub_nums(num1, num2):
    return num1 - num2

# Subtract two numbers such that the smaller number is always subtracted from the bigger number
def abs_diff(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return num1 - num2
