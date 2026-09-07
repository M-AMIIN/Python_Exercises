import random
#user picks a max number
top_of_range = input("Type a number: ")

#checks if input is actually a number 
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("type a number larger than 0 next time. ")
        quit()
else:
    print("type a number larger than 0 next time. ")
    quit()

random_numb = random.randint(0, top_of_range)
print(random_numb) 