def check_guess(guess, answer):
    global score

    if guess.lower() == answer.lower():
        print("Correct Answer")
        score = score + 1
            
    else:
        print("Sorry Wrong Answer!")
    print("The Correct answer is ",answer )
    
score = 0
print("Guess: TRUE Or FALSE ")
guess1 = input("1.A COVID-19 vaccine will have a microchip embedded in it.\n")
check_guess(guess1, "False")
guess2 = input("2.Vaccines can change your DNA.\n")
check_guess(guess2, "False")
guess3 = input("3.The flu shot prevents COVID-19.\n")
check_guess(guess3, "False")
print("Your Score is "+ str(score))