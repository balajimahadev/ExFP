# importing date class from datetime module
from datetime import date

# Exercise 1-6

# Ex1
name = input("What is your name?")
print("Hello", name, "Nice to meet you !")

# Ex2
inputstr = input("What is the input string?")
print(inputstr, "has", len(inputstr), "characters.")

# Ex3
inputquote = input("What is the quote?")
inputperson = input("Who said it?")
print(inputperson, "says", '"', inputquote, '"')

# Ex4
inputnoun = input("Enter a noun: ")
inputverb = input("Enter a verb: ")
inputadjective = input("Enter a adjective: ")
inputadverb = input("Enter a adverb: ")

print("Do you", inputverb,  "your", inputadjective,
      inputnoun, inputadverb, "?", "That's hilarious!!!")

# Ex5
firstnum = input("What is the first number?")
secondnum = input("What is the second number?")


txt = "{} + {} = {}"
result = int(firstnum) + int(secondnum)
print(txt.format(firstnum, secondnum, result))

txt = "{} - {} = {}"
result = int(firstnum) - int(secondnum)
print(txt.format(firstnum, secondnum, result))

txt = "{} * {} = {}"
result = int(firstnum) * int(secondnum)
print(txt.format(firstnum, secondnum, result))

txt = "{} / {} = {}"
result = int(int(firstnum) / int(secondnum))
print(txt.format(firstnum, secondnum, result))

# Ex6


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


age = get_non_negative_int("What is your current age? ")
retire_age = get_non_negative_int("At what age would you like to retre? ")

years_left = int(retire_age) - int(age)

if years_left > 0:
    print(" you have {} years left until you can retire".format(years_left))
    current_date = date.today()
    print(" It's {}, so you can retire in {}".format(
        current_date.year, (current_date.year + int(years_left))))
else:
    print("You should already be retired")
