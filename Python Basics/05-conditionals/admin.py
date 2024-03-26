users = []

if not users:
    print("No users Found")

else:

    for user in users:
        if user.lower() == "admin":
            print("Hello " + user.title()  + ", Want to see some details?")
        else:
            print("Hello " + user.title() + ", Good to see you back")