#Creating a random password generator that I found from a tutorial online. Cool!
#Going to document each step

#Import the random module
import random

#Intial setup
print("Welcome to the Password Generator!")

#Create the variables
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"
number = input("Amount of passwords to generate: ")
number = int(number)
length = input("Input your password length: ")
length = int(length)

#After variables are entered, start next print statement
print("\nHere are you passwords:")

#Create loop for code
for pw in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

print("\nNOICE!!")
