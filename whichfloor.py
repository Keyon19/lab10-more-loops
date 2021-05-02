maximum_stories = 10
userinput = input("On what floor of the building is your office?")
usernum = int(userinput)

while usernum<maximum_stories:
    print("Enter another number please")
    userinput = input("On what floor of the building is your office?")
    usernum = parseInt(userinput)



print("Congrats, " + usernum + "is a valid number")
