userstring = input("Gimme a number that is greater than 100...")
usernum = int(userstring)

while usernum<100:
    print(str(usernum) + "is less than 100, try again I got all day...")
    userstring = input("Gimme a number that is greater than 100...")
    usernum = str(userstring)


print(str(usernum) + "is greater than 100, Finally, Great job")
