# 1 lister menyen
hovedrett1 = "Biff"
hovedrett2 = "Laks"
vegetarrett = "Bønner"
grønnsakstilbehør = "Potet"
saustilbehør = "bearnaise"

# 2 ber bruker om å velge rett og tilbehør
førstehovedrett = input("Velg en hovedrett: ")
førstetilbehør = input("Velg et tilbehør: ")

# 3 sjekker betingelser for uten grønnsaker
if førstehovedrett != vegetarrett and førstehovedrett != grønnsakstilbehør:
    print("Du spiser ikke nok grønnsaker!")

# sjekker for kun grønnsaker
if (førstehovedrett == vegetarrett and førstetilbehør == grønnsakstilbehør):
    print("Du har valgt et vegetarmåltid")

# sjekker for kombinasjon av grønnsaker og ikke vegetarsk måltid
if (førstehovedrett == vegetarrett and førstetilbehør != grønnsakstilbehør) or (førstetilbehør == grønnsakstilbehør and førstehovedrett != vegetarrett):
    print("Du har valgt " + førstehovedrett + " med " + førstetilbehør)
    
