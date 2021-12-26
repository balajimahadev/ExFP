# Ex 14-23
import getpass
import bcrypt

# Tax Calculator


def tax_calculation():
    amount = int(input("What is the order amount? "))
    state = input("What is the state?")

    if state.casefold() == "WI".casefold() or state.casefold() == "wisconsin".casefold():
        print("The subtotal is ${}".format(amount))
        print("The tax is ${}".format(float(amount*0.055)))
        print("The total is ${}".format(float(amount + amount*0.055)))
    else:
        print("The total is ${}".format(amount))


# tax_calculation()


# Password authenticator
def password_valid():

    dict_pass = {'nousr': 'nopass'}
    salt = bcrypt.gensalt()

    while True:

        create_user = 1 if input(
            "Create user? Y/N ?").casefold() == "Y".casefold() else 0

        print(create_user)
        if create_user:
            username = input("Input Username : ")
            passwd = getpass.getpass(prompt='Password: ', stream=None)
            hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt)
            dict_pass[username] = hashed

        else:
            get_usrname = input("Which user:")
            get_passwd = getpass.getpass(prompt='Password: ', stream=None)

            if bcrypt.checkpw(get_passwd.encode('utf-8'), dict_pass[get_usrname]):
                print("Authenticated")
            else:
                print("Denied")

        exit_program = 1 if input(
            "Exit Program? Y/N ?").casefold() == "Y".casefold() else 0

        if exit_program:
            break


password_valid()



# Ex Number to names
def number_to_names():

    number = input("Please enter the number of the month: ")

    return {
        '1': "January",
        '2': "February",
        '3': "March",
        '4': "April",
        '5': "May",
        '6': "June",
        '7': "July",
        '8': "August",
        '9': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }[number]


print(number_to_names())
