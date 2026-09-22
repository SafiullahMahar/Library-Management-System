User_name = input("Enter the username:")
Password = int(input("Enter the password:"))

def login():
    if User_name == "Safi" and Password == 1234:
        print("Login Successful!")

    else:
        print("Something went wrong!")

login()
