def Greeting (message):
    more_people = input("Is there another person to greet? Type y for yes and n for no.")     
    more_people = more_people.lower()

    while (more_people == "y"):
        name = input("What is your coworker's name?")
        print(message, name + "!") # instead of using a hard coded message, we use the passed in one
        more_people = input("Is there another person to greet? Type y for yes and n for no.")
        more_people = more_people.lower()

Greeting ("Good morning")
# do some work till lunch time
print("It's lunchtime!")

Greeting ("See you after lunch")
# return from lunch
print("Back to work...")
# work till end of day
print("Finally, working day is through!")

Greeting ("Goodbye")