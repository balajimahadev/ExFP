import requests
import json


# Exercises 7-12

# # Ex 7
# CONV_FEET_2_METRES = 0.09290304

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry i don't understand that")

        if value < 0:
            print("The dimensions cannot be negative")
        else:
            break
    return value


# length = get_non_negative_int("What is the length of the room in feet?")
# breadth = get_non_negative_int("What is the length of the room in feet?")

# print("you entered dimesnions of {} feet by {} feet".format(length, breadth))

# area_feet = length * breadth
# area_metre = area_feet * CONV_FEET_2_METRES

# print("The area is")
# print("{} square feet".format(area_feet))
# print("{} square metres".format(area_metre))


# #Ex 8
# num_people = get_non_negative_int("How many people at the party?")
# num_pizza = get_non_negative_int("How many pizza's ?")
# num_slices = get_non_negative_int("How many slices per pizza?")

# print("{} people with {} slices of pizza".format(num_people, num_slices))
# total_slices = num_pizza * num_slices
# per_person = int(total_slices / num_people)
# rem_slices = int(total_slices % num_people)
# print("Each person gets {} pieces of pizza".format(per_person))
# print("There are {} leftover pieces".format(rem_slices))


# Ex9

ONE_GALLON = 350

length = get_non_negative_int("What is the length of the room in feet?")
breadth = get_non_negative_int("What is the length of the room in feet?")

print("you entered dimesnions of {} feet by {} feet".format(length, breadth))

area_feet = length * breadth

req = int(area_feet/ONE_GALLON) + int(1 if ( % ONE_GALLON) > 0 else 0)

print(" you will need to purcahse {} gallomns of paint to cover {} square feet".format(
    area_feet, req))

def validate_input(prompt):
    while True:
        try:
            numeric_input = int(input(prompt))
        except ValueError:
            print("Sorry, that is not a valid input")

        if numeric_input < 0:
            print("Please enter a positive value")
        else:
            break
    return numeric_input

def selfcheckout():
    items = list()
    price = list()

    count = 3
    while count > 0:
        items.append(validate_input("add quantity of item {}: ").format())
        price.append(validate_input("add price of item {}: ").format())
        count -= 1

    sumlist = [x * y for (x, y) in zip(items, price)]
    print(sumlist)

    sumtotal = sum(sumlist)*1.055

    print(sumtotal)

# selfcheckout()

def currency_converter():
    url = 'https://v6.exchangerate-api.com/v6/eb5625de50362978e04f4bd8/latest/EUR'
    response = requests.get(url)
    data = response.json()
    curr_data = json.loads(json.dumps(data))

    euros_to_convert = validate_input("How many euros are you exchanging?")
    usd_value = euros_to_convert * curr_data['conversion_rates']['USD']
    print(usd_value)


# currency_converter()

def simple_interest():

    principal = validate_input("Enter the principal amount")
    interest = float(input("Enter the rate of interest"))
    duration = validate_input("Enter the number of years")

    output = principal + float((principal*interest*duration)/100)

    print("After {} years at {}% the investment will be worth ${}".format(
        duration, interest, output))

# simple_interest()


def compound_interest():
    principal = validate_input("Enter the principal amount")
    interest = float(input("Enter the rate of interest"))
    duration = validate_input("Enter the number of years")
    periods = validate_input("Enter the number of periods")

    output = round (principal * (1 + (interest/(periods*100)))**(duration*periods), 3)

    print("After {} years at {}% the investment will be worth ${}".format(
        duration, interest, output))

compound_interest()
