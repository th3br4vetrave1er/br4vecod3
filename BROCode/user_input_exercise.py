username = input("Enter your username: ")

if len(username) > 12:
    print("Username must contain under 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome, {username}!")