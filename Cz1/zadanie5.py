imie=input("Podaj swoje imię: ")

rok_ur=int(input("Podaj swój rok urodzenia: "))


if 2022 - rok_ur>17:
    kohol=str("jesteś pełnoletni")
else:
    kohol=str("nie jesteś pełnoletni")

print(imie+", masz",2022 - rok_ur," lata, "+kohol)