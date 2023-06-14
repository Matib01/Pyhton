a=float(input("Podaj pierwszą długość: "))
b=float(input("Podaj drugą długość: "))
c=float(input("Podaj trzecią długość: "))
if a+b>c and b+c>a and c+a>b:
    print("Można stworzyć trójkąt z podanych długości")
else:
    print("Nie można stworzyć trójkąta z podanych długości")