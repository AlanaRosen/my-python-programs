def calculate(check,tip,name):
    total_check = (check * (tip/100) + check)
    total_check = round (total_check, 2)
    print ("\n" + str(name) + ", if you would like to tip ", str(tip) + "%, then your total will be $" + str(total_check) + ".")
    
def others():
    while start == "yes":
        name = input("\nWhat name would you like to use? ")
        check = float (input ("\nWhat was the total for your check? $"))        
        if check > 0:
            tip = float (input ("\nWhat percentage would you like to tip? "))
            calculate(check,tip,name)
            more = input("\nIs there anyone else who would like to calculate their tip? Please answer 'yes' or 'no' accordingly. ")
            more = more.lower()
        else:
            print("Yeah, you're not doing this correctly, buddy. Try again.")
            others()
    
start = input ("Is there someone who would like to calculate a tip? Please answer 'yes' or 'no' accordingly. ")
start = start.lower()

others()