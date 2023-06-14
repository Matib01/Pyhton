

i=0
lista=[]
suma=0

ilosc=int(input("Ile chcesz podać liczb? : "))
if ilosc<1:
    print("Podałeś niepoprawną wartość")
else:
    while i<ilosc:
        lista.append(int(input("Podaj liczbę: ")))
        suma=suma+lista[i]
        i=i+1
    print(lista)
    print("Suma liczb = ",suma)