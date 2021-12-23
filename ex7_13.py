import requests
import json

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
