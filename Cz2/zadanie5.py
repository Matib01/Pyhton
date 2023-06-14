liczba=59
licznik=0

while True:
    odgadnij=int(input("Podaj liczbę: "))
    licznik+=1
    if odgadnij>59:
        print("Szukana wartość jest mniejsza")
    elif odgadnij==59:
        print("Gratulacje wygrałeś !!! Twoja liczba prób wyniosła: ",licznik)

        break
    else:
        print("Szukana wartość jest większa")