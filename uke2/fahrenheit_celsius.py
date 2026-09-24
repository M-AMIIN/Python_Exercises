
'''
fahrenheit = int(input("Hvor mange grader er det i fahrenheit? "))

celsius = (fahrenheit - 32)*5/9

print(f"{fahrenheit} grader fahrenheit er {celsius} grader celsius")
'''
temp = int(input("Oppgi tempraturen du ønsker: "))

enhet = input("Oppgi om enhet, fahrenheit(F) eller celsius(C). (F/C) ")

if enhet == "F":
    celsius = (temp - 32)*5/9
    print(celsius)
elif enhet == "C":
    fahrenheit = (temp/5) * 9 + 32
    print(fahrenheit)
else:
    print("Skriv inn gyldig input!")