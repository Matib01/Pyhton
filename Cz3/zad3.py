
x=0

lista=[]
min=None
max=None



ilosc=int(input("Ile chcesz podać liczb? : "))
if ilosc<1:
    print("Podałeś niepoprawną wartość")
else:
    while x<ilosc:
        lista.append(int(input("Podaj liczbę: ")))
        x=x+1
    print(lista)

    for i in lista:
        if min == None or min > i:
            min = i
        if max == None or max < i:
            max = i

    print("max to: ", max)
    print ("min to: ",min)


