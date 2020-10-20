#Rock,Paper,Scissors
from random import randint
t=["Alvin","Defri","Adrian","Refki","Ananda","Friska"]
acak=t[randint(0,5)]
print(acak)
anak= False
while anak== False:
    anak = input("Anak ke ")
    if acak=="Alvin" and anak=="5":
        print(True)
    elif acak=="Ananda" and anak=="6":
        print(True)
    elif acak=="Defri" and anak=="1":
        print(True)
    elif acak=="Friska" and anak=="4":
        print(True)
    elif acak=="Refki" and anak=="3":
        print(True)
    elif acak=="Adrian" and anak=="2":
        print(True)
    else : print(False)
    anak= False
    acak=t[randint(0,5)]
    print(acak)