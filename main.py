logged_in = False
not_terminated = True

import sys


def information_checker(first_name, last_name, pincode):
    if len(pincode) <= 4 and first_name != "" and last_name != "":
        return True
    else:
        return False


def valid_option_selection(selection):
    if selection == "a" or selection == "b" or selection == "c":
        return True
    else:
        return False


while not_terminated:
    if not logged_in:
        create_account = input("Looks like you don't have an account - do you want to create an account? (YES or NO) ")

        if create_account.__contains__("yes") or create_account.__contains__("YES"):

            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            pincode = input("Enter a four-digit pin: ")

            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "pincode": pincode,
                "account_balance": 0
            }

            while not information_checker(first_name, last_name, pincode):
                print("Invalid pin. Please re-enter your information")
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                pincode = input("Enter a four-digit pin: ")

                user_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "pincode": pincode,
                    "account_balance": 0
                }

            print("Hello", user_data["first_name"], user_data["last_name"], "welcome to your financial dashboard")

        elif create_account.__contains__("no") or create_account.__contains__("NO"):
            print("Thank you for your time!")
            sys.exit()

    print("a. Check balance")
    print("b. Deposit Funds")
    print("c. Withdraw Funds")
    print("d. Logout")

    user_choice = input()

    if user_choice == "a":
        print("Hi ", user_data["first_name"], "you have $", user_data["account_balance"])
    elif user_choice == "b":
        user_amount_deposit = input("Hi " + user_data["first_name"] + ",how much would like to deposit?")

        user_data["account_balance"] = user_data["account_balance"] + user_data["account_balance"]
        print(user_data["account_balance"])
    elif user_choice == "c":
        user_amount_withdraw = input("Hi " + user_data["first_name"] + ",how much would like to withdraw?")
    elif user_choice == "d":
        not_terminated = False

    else:
        while not valid_option_selection(user_choice):
            print("Hey " + user_data["first_name"], ", that was not a valid option. Please enter a valid option.")
            user_choice = input()
            if user_choice == "a":
                print("Hi Pranav, you have $", user_data["account_balance"])
            elif user_choice == "b":
                user_amount_deposit = input("Hi " + user_data["first_name"] + ",how much would like to deposit?")

                user_data["account_balance"] = user_data["account_balance"] + user_data["account_balance"]
                print(user_data["account_balance"])

            elif user_choice == "c":
                user_amount_withdraw = input("Hi " + user_data["first_name"] + ",how much would like to withdraw?")
            elif user_choice == "d":
                not_terminated = False
