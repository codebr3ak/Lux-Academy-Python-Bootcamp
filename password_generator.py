#Import the necessary modules
import random 
import string

print('Hello, Weo=lcome to the Password Generator')

#Input the length of the password
length = int(input('\nEnter the length of the password:'))

#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation