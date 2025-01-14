#Quiz Game


questions=("How many elements in the periodic table?:","Which is the most abundant element?:","Which animal lays the largest eggs?:","How many bones in the human body?:","Which is the most abundant gas in the air?:")
options=(("A.190","B.118","C.90","D.500"),
         ("A.Hydrogen","B.Gold","C.Uranium","D.Oxygen"),
         ("A.Chicken","B.Snake","C.Osctrich","D.Crocodile"),
         ("A.100","B.50","C.206","D.250"),
         ("A.Nitrogen","B.Oxygen","C.Helium","D.Sulphur"))
answers=("B","A","C","C","A")
guesses=[]
score=0
question_no=0


for question in questions:
    print("* * * * * * * * ")
    print(question)
    for option in options[question_no]:
        print(option)

    guess=input("Enter your guess: ").upper()
    guesses.append(guess)

    if guess==answers[question_no]:
        score+=1
        print("CORRECT!!!")
    else:
        print("INCORRECT!!!")
    question_no+=1


print(f"Your score is {score}/5")
print()
print("------------End of Quiz------------")




