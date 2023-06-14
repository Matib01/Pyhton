
i=0
lista=[]


ilosc=int(input("Ile chcesz podać liczb? : "))
if ilosc<1:
    print("Podałeś niepoprawną wartość")
else:
    while i<ilosc:
        lista.append(int(input("Podaj liczbę: ")))
        i=i+1
    print(lista)
    