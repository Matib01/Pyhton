
suma=0
ilosc=0
lista=[]

while True:
    wprowadzona_liczba=input("Wproawdz swoja liczbe: ")
    if wprowadzona_liczba=="end":
        if ilosc==0:
            print("Błąd, wprowadziłeś end za wcześnie !")
            break
        print(lista)
        print("Twoja suma to: ",suma)
        break
    else:
        lista.append(wprowadzona_liczba)
        suma +=  float(wprowadzona_liczba)
        ilosc += 1


