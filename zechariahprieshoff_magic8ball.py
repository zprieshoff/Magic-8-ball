#Zechariah Prieshoff
#Magic 8 ball
#May 13th, 2024
#This program will work like an online 8 ball. The user asks a question and gets a fortune.

import random

print("Welcome to the python 8 ball! \n     =================")

print("Here's what you can do:")
print("1. Show me all the fortunes.\n2. I want to choose a fortune.\n3. I want to ask a question.\n4. Show me some example questions. ")
choice = input("What would you like to do? (Enter 1, 2, 3, or 4): ")

if choice == "1":
    print("Here's a list of all the fortunes. \n--------------")
    print("1. Absolutely \n2. No way \n3. Yes \n4. Maybe not \n5. Definitely \n6. Not at all \n7. Sure \n8. I don't think so \n9. Maybe \n10. Not this time \n--------------")
    
elif choice == "2":
    choiceFortune = input("\nPlease enter a number between 1 and 10: ")
    if choiceFortune == "1":
        print("Your fortune is: Absolutely")
    elif choiceFortune == "2":
        print("Your fortune is: No way")
    elif choiceFortune == "3":
        print("Your fortune is: Yes")
    elif choiceFortune == "4":
        print("Your fortune is: Maybe not")
    elif choiceFortune == "5":
        print("Your fortune is: Definitely")
    elif choiceFortune == "6":
        print("Your fortune is: Not at all")
    elif choiceFortune == "7":
        print("Your fortune is: Sure")
    elif choiceFortune == "8":
        print("Your fortune is: I don't think so")
    elif choiceFortune == "9":
        print("Your fortune is: Maybe")
    elif choiceFortune == "10":
        print("Your fortune is: Not this time")
    else:
        print("Sorry, that's not an option.")

elif choice == "3":
    question = input("What's your question? \n")
    if not question.endswith("?"):
        print("That's not a question, idiot.")
    else:
        fortuneRandom = random.choice(["Absolutely", "No way", "Yes", "Maybe not", "Definitely", "Not at all", "Sure", "I don't think so", "Maybe", "Not this time"])
        print(f"Your fortune is: {fortuneRandom}")
        
elif choice == "4":
    print("Here's some example questions to get your brain rollin' \n--------------")
    print("Will my car be driveable next week? \nWill I stub my toe when I get home from work? \nAm I real? \nShould I make Linguini tonight? \n--------------")

else:
    print("Sorry, that's not an option.")