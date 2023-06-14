lp=int(input("Podaj liczbę punktów: "))
forma=int(input("Wybór formy (Podaj numer):\n 1:Liczbowo\n2:słownie\n3:oba\n"))

if lp<50:
    ocena=2.0
    ocena_s="niedostateczny"
elif lp<60:
    ocena=3.0
    ocena_s="dostateczny"
elif lp<70:
    ocena=3.5
    ocena_s="dostateczny plus"
elif lp<80:
    ocena=4.0
    ocena_s="dobry"
elif lp<90:
    ocena=4.5
    ocena_s="dobry plus"
elif lp<100:
    ocena=5
    ocena_s="bardzo dobry"
else:
    ocena=5.5
    ocena_s="celujący"

if forma==1:
    print("Wybrałeś ocene liczbowo: ",ocena)
elif forma==2:
    print("Wybrałeś ocene słownie: ",ocena_s)
else:
    print("Ocena liczbowo: ",ocena)
    print("Ocena słownie: ",ocena_s)
