master_pwrd = input("Type in master password: ")

def view():
    with open('Passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, ", Password:", passw)

def add():
    name = input('Account name: ')
    pwrd = input('Password: ')

    with open('Passwords.txt', 'a') as f:
        f.write(name + "|" + pwrd + "\n")


while True:
    mode = input("Do you want to add a new password or view existing ones (view, add)? press (q) to quit! ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue

