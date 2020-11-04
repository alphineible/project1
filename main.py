#Jempol,Telunjuk,Kelingking
from random import randint
t=["Jempol","Telunjuk","Kelingking"]
acak=t[randint(0,2)]
print("Masukkan Jari")
jari= False
while jari== False:
    jari = input("")
    if acak=="Jempol" :
        if jari=="Jempol":
            print('x')
            print(acak)
            print("Hahaha Seri")
        elif jari=="Telunjuk":
            print('x')
            print(acak)            
            print("Maaf:(, kamu Kalah")
        elif jari=="Kelingking":
            print('x')
            print(acak)            
            print("Yeay, kamu Menang!")
    elif acak=="Telunjuk" :
        if jari=="Jempol":
            print('x')
            print(acak)
            print("Yeay, kamu Menang!")
        elif jari=="Telunjuk":
            print('x')
            print(acak)            
            print("Hahaha Seri")
        elif jari=="Kelingking":
            print('x')
            print(acak)            
            print("Maaf:(, kamu Kalah")
    elif acak=="Kelingking" :
        if jari=="Telunjuk":
            print('x')
            print(acak)            
            print("Yeay, kamu Menang!")
        elif jari=="Kelingking":
            print('x')
            print(acak)
            print("Hahaha Seri")
        elif jari=="Jempol":
            print('x')
            print(acak)
            print("Maaf:(, kamu Kalah")
    else : print(False)
    jari= False
    acak=t[randint(0,2)]
    print("__________")
    print("Masukkan Jari")
