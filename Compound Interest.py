def stupid(placeholder):
  total = placeholder * (1+ .04/12)**12
  return (str(round (total, 2)))  

deposit = float(input("What amount of money did you deposit? Just enter the number, please. "))
total = stupid(deposit)
print("Your total after interest is now: $" +total)

deposit_gary = float (input ("How much did Gary put in his bank? "))
total = stupid(deposit_gary)
print ("Gary's total is now: $" +total)

