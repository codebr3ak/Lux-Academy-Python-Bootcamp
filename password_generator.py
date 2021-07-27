#Import the necessary modules
import random 
import string

print('Hello, Welcome to the Password Generator')

#Input the length of the password
length = int(input('\nEnter the length of password: '))    

#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#Combine all the data
all = lower + upper + num + symbols

#Use random 
temp = random.sample(all,length)

#Create the password
password = "".join(temp)

#Print the password
print(password)
