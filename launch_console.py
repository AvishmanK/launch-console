name = input("What is your name?: ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print ("3) Favorite project")
    print("4) Exit")
    choice = (input("Pick 1-4: "))
    if choice == "1":
        about_me = input("Write About you: ")
        print("About me: " + about_me)
    elif choice == "2":
        my_goals = input("Write about your goals: ")
        print("My goals: " + my_goals)
    elif choice == "3":
        fav_proj = input("Write about your favorite project: ")
        print("Favorite project: " + fav_proj)
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1,2,3, or 4.")


