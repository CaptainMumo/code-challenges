def password_checker(password):
    characters = "$#@"
    if len(password) >= 6:
        if len(password) <= 12:
            if any(x.islower() for x in password):
                if any(x.isupper() for x in password):
                    if any(x.isdigit() for x in password):
                        if any(x in characters for x in password):
                            return "Hooray! The password is valid"
                        else:
                            return "Password should contain at least 1 character from [$#@]"
                    else:
                        return "Password should contain at least 1 number"
                else:
                    return "Password should contain at least 1 upper case letter"
            else:
                return "Password should contain at least 1 lower case letter"
        else:
            return "Password should be at most 12 characters long"
    else:
        return "Password should be at least 6 characters long"


if __name__ == "__main__":

    print("\nPassword should contain :\n"\
            "\nAt least 1 lower case letter"\
            "\nAt least 1 upper case letter"\
            "\nAt least 1 number"\
            "\nAt least 1 character from [$#@]"\
            "\nAt least 6 characters"\
            "\nAt most 12 characters")
    while True:
        password = input("\nEnter your password : ")
        print()
        print(password_checker(password))
        if password_checker(password) == "Hooray! The password is valid":
            break
