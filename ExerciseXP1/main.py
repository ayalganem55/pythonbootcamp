#Excercise 1
from random import Random, random
from tkinter.tix import TCL_ALL_EVENTS


def display_message():
    print("I am learning Functions on Python")

display_message()

#Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

book = input("Which is your favorite book?: ")
favorite_book(book)

#Exercise 3
def describe_city(city, country):
    print(f"{city} is in {country}")

my_country = "Argentina"
my_city = "Rosario"
describe_city(my_city, my_country)

#Exercise 4
import random
def casino(num,lucky):
    if num != lucky:
        print(lucky)
        print("Good luck next time")
    else:
        print("You win mutherfucker")

number = int(input("Tell me a num:"))
lucky_number = random.randint(1,100)
casino(number, lucky_number)

#Exercise 5
def make_shirt(size,message):
    print(f"the size of the shirt is {size} and the message is {message}")

talle = input("What is the shirt's size?")
mensaje = input("What message do you want to print on your shirt?")
make_shirt(talle, mensaje)

#Exercise 6
wizards = ["Harry", "Ron", "Hermarione", "Malfoy", "Voldemort", "Dumbeldore","Newt","Sirius","Neville"]
def show_wizards():
    for wizard in wizards:
        print (wizard)

show_wizards(wizards) # You have a bug here, the function show_wizards didn't get any parameter, please fix it.
