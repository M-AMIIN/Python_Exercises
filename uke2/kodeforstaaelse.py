
a = input("Tast inn et heltall! ")
b = int(a)

if b < 10:
    print (b + "Hei!")
'''
1. Vil programmet ovenfor kjøre? Begrunn svaret.
Programmet ovenfor vil kjøre, men fordi den konverter en string til 
integer og deretter prøver å legge sammen en string og en int vil den krasje om
betingelsen er sann. 
2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
om heltallet er under 10 vil programmet vise feilkjøring. 
'''