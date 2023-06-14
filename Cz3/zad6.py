zdanie=[]
zdanie = input("Podaj zdanie: ")
len=len(zdanie)
slownik={}

for i in range(len):
    slownik[zdanie[i]]= zdanie.count(zdanie[i])
slownik.pop(' ')
print(slownik)