# author : dofisaputra
# game batu kertas gunting

import random

def pilih_hand (hand):
    if hand < 1 or hand > 3:
        return False
    return True

def hasil (player_hand, computer_hand):
    if player_hand == computer_hand:
        return "Seri!"
    elif player_hand == 1 and computer_hand == 2:
        return user_name + " Kalah!"
    elif player_hand == 2 and computer_hand == 3:
        return user_name + " Kalah!"
    elif player_hand == 3 and computer_hand == 4:
        return user_name + " Kalah!"
    else:
        return user_name + " Menang!"

list_hand = ["kosong", "Batu", "Kertas", "Gunting"]

ulang = "y"
while (ulang == "y" or ulang == "Y"):
    print ("")
    print ("Game Batu Kertas Gunting")
    print ("-------------------------")
    print ("")
    user_name = input("Username : ")
    print ("")
    print ("---------------")
    print ("[1] Batu")
    print ("[2] Kertas")
    print ("[3] Gunting")
    print ("---------------")
    print ("")
    player_hand = int(input("Pilih Salah Satu Pilihan Diatas (1,2, atau 3) : "))
    print ("")

    if pilih_hand(player_hand):
        computer_hand = random.randint(1,3)
        
        print ("---------------------------")
        print (user_name + " Memilih : " + list_hand[player_hand])
        print ("Computer Memilih : " + list_hand[computer_hand])

        print ("Hasil : " + hasil(player_hand, computer_hand))
        print ("---------------------------")

        print ("")
        ulang = input ("Main Lagi? (y/n) : ")

        if (ulang == "n" or ulang == "N"):
            break

        else:
            while (ulang != "y" and ulang != "n"):
                print ("Masukan huruf y atau n!")
                ulang = input("Mulai? (y/n) : ")

    else:
        print ("Masukan Angka 1-3!")
        print ("------------------")
        while (player_hand != 1 and player_hand != 2):            
            print ("")
            print ("Ulang Game? [1] yes [2] no")
            player_hand = int(input("Masukan Pilihan (1/2) : "))
            if (player_hand == 2):
                ulang = "n"
        
print ("")
print ("-------------")
print ("|  Bye Bye  |")
print ("-------------")
print ("")        
