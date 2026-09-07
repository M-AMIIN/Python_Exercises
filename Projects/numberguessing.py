import random
#user picks a max number
top_of_range = input("Type a number for guessing range: ")

#checks if input is actually a number 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
# makes sure top of range is larger than 0
    if top_of_range <= 0:
        print("type a number larger than 0 next time. ")
        quit()
else:
    print("type a number larger than 0 next time. ")
    quit()

random_numb = random.randint(0, top_of_range)
guesscount = 0

while True:
    guesscount += 1
    userG = input("Guess a number: ")
    if userG.isdigit():
        userG = int(userG)
    else:
        print("type a number larger than 0 next time. ")
        continue 
#checks if guess matches random number, if not checks if guess is more or less than the number. 
    if userG == random_numb:
        print("CORRECT NUMBER! ")
        break
    elif userG > random_numb:
            print("WRONG NUMBER. You were above the CORRECT number ")
    else:
        print("WRONG NUMBER. You were below the CORRECT number ")

print(f"You guessed the correct number in {guesscount} guess(es)!")

    

