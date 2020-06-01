# # 2.soru:
import random
b = []
while len(b) < 6:
    e = random.randint(1,50)
    if e not in b:
        b.append(e)
print(b)

# 3.soru:
b=0
e=input("en fazla iki basamakli bir sayi girin: ")
y = open("1904107005.beyzatuzcu.py",'w')
if int(e)<100 and int(e)>1 :
    for i in range(1,int(e)) :
        z=i//10
        a=i%10
        b=z+a
        if b % 2 == 1 :

            y.write( str(i)+"=" +str(b) +"  tek sayi oldugu icin dosyaya yazilir."+ "\n")

        else:
            continue
    y.close()
else:
    print("hata oldu...")

# #SORU4:
from functools import reduce

b=['Aygun','Çiçek','Deniz','Atar','Dener','Yılmaz']
e= [['Ayse', 3,6,7],['Ece', 5,2,4],['Arya', 6,5],['Ali', 3],['Can',5,7,9,11],['Aybar',2,3]]
y=list(map(lambda z,:[z[0]+" "+b[0]] + [reduce(lambda a,b: a+b , z[1:])],  e))
print("Elde etmemiz gereken sonuc = ",y)
