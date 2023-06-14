r=int(input("Podaj promień: "))
import math

if r<=0:
    print("Promień nie może być ujemny!!!")
else:
    pole=round(math.pi*r**2,ndigits=2)
    obwod=round(2*math.pi*r,ndigits=2)
    print("Pole koła: ",pole,"\nObówd koła: ",obwod)
