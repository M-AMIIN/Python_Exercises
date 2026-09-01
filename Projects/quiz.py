# Python quiz game

questions = ("How many countries are there in Europa?: ", 
            "How many countries are there in Asia?: ",
            "How many countries are there in Afrika?: ",
            "How many countries are there in Amerika?: ")

options = (("A. 44", "B. 89 ", "C. 50 ", "D. 17 "),
           ("A. 95", "B. 48 ", "C. 53 ", "D. 42 "),
           ("A. 44", "B. 23 ", "C. 54 ", "D. 25 "),
           ("A. 23", "B. 49 ", "C. 58 ", "D. 35 "))

answers = ("A", "B", "C", "D")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()

    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("CORRECT")
    else: 
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer! ")

    question_num = question_num + 1

print(f"GAME OVER! TOTAL POINTS ARE: {score}")
print()
print("Correct answers are: ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"your score is: {score}%")

