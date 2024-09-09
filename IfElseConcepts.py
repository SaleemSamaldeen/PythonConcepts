userName = input("Enter your username: ")
if len(userName) > 12:
    print("username length is more than 12 characters")
elif not userName.isalpha():
    print("username can't contain numbers or spaces")
elif not userName.find(" ") == -1:
    print("username can't contains spaces")
