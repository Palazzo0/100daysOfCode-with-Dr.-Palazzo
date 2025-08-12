temp = float(input("Enter Body Temperature"
                   " in degree celsius"))
#HERE COMES THE CONDITIONAL STATEMENT
if temp >= 38:
    print("You might have a fever🥵")
elif 36<= temp < 38:
    print("Your temperature is normal.👍")
else:
    print("That's lower than normal. Are "
          "you okay?")