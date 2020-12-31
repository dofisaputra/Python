# atuhor : dofisaputra
# game tic tac toe

import random, sys

papan_permainan = {"A1": "   ", "A2": "   ", "A3": "   ", "B1": "   ", "B2": "   ", "B3": "   ", "C1": "   ", "C2": "   ", "C3": "   "}

def hasil():
    # versi player
    # horizontal
    if papan_permainan["A1"] == " X " and papan_permainan["A2"] == " X " and papan_permainan["A3"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["B1"] == " X " and papan_permainan["B2"] == " X " and papan_permainan["B3"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["C1"] == " X " and papan_permainan["C2"] == " X " and papan_permainan["C3"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    # vertikal
    elif papan_permainan["A1"] == " X " and papan_permainan["B1"] == " X " and papan_permainan["C1"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A2"] == " X " and papan_permainan["B2"] == " X " and papan_permainan["C2"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A3"] == " X " and papan_permainan["B3"] == " X " and papan_permainan["C3"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    # diagonal
    elif papan_permainan["A1"] == " X " and papan_permainan["B2"] == " X " and papan_permainan["C3"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A3"] == " X " and papan_permainan["B2"] == " X " and papan_permainan["C1"] == " X ":
        print ("------------")
        print ("Kamu Menang!")
        print ("------------")
        print ("")
        return 0

    # versi computer
    # horizontal
    elif papan_permainan["A1"] == " O " and papan_permainan["A2"] == " O " and papan_permainan["A3"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["B1"] == " O " and papan_permainan["B2"] == " O " and papan_permainan["B3"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["C1"] == " O " and papan_permainan["C2"] == " O " and papan_permainan["C3"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    # vertikal
    elif papan_permainan["A1"] == " O " and papan_permainan["B1"] == " O " and papan_permainan["C1"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A2"] == " O " and papan_permainan["B2"] == " O " and papan_permainan["C2"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A3"] == " O " and papan_permainan["B3"] == " O " and papan_permainan["C3"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    # diagonal
    elif papan_permainan["A1"] == " O " and papan_permainan["B2"] == " O " and papan_permainan["C3"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    elif papan_permainan["A3"] == " O " and papan_permainan["B2"] == " O " and papan_permainan["C1"] == " O ":
        print ("------------")
        print ("Kamu Kalah!")
        print ("------------")
        print ("")
        return 0
    return 1

def petuntuk_game():
    print ("Petunjuk Permainan :")
    print ("Masukan Salah Satu Code Dibawah")
    print ("========================")
    print ("||  A1  |  A2  |  A3  ||")
    print ("||--------------------||")
    print ("||  B1  |  B2  |  B3  ||")
    print ("||--------------------||")
    print ("||  C1  |  C2  |  C3  ||")
    print ("========================")
    print ("")
    print ("-------------")
    print ("Player   : X ")
    print ("Computer : O ")
    print ("-------------")
    print ("")

list_pilihan = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
list_pilihan_player = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
list_pilihan_computer = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

cek_hasil = 1
pemain = 1
game_jalan = 0
nomor_player = 0
nomor_computer = 0

# tampilan game

try:

    print ("")
    print ("-----------------")
    print ("Game Tic Tac Toe")
    print ("-----------------")
    print ("")

    petuntuk_game()

    while True:
        print ("=====================")
        print ("|| " + papan_permainan["A1"] + " | " + papan_permainan["A2"] + " | " + papan_permainan["A3"] + " ||")
        print ("||-----------------||")
        print ("|| " + papan_permainan["B1"] + " | " + papan_permainan["B2"] + " | " + papan_permainan["B3"] + " ||")
        print ("||-----------------||")
        print ("|| " + papan_permainan["C1"] + " | " + papan_permainan["C2"] + " | " + papan_permainan["C3"] + " ||")
        print ("=====================")
        print ("")

        cek_hasil = hasil()

        if game_jalan == 9 and cek_hasil == 1:
            print ("----------")
            print ("Hasil Seri")
            print ("----------")
            print ("")
            break
        elif cek_hasil == 0:
            break
        
        while True:
            if pemain == 1:
                pemain_input = input("Masukan Pilihan Anda : ")
                pemain_input = pemain_input.upper()

                while (pemain_input == list_pilihan_computer[0] or pemain_input == list_pilihan_computer[1] or pemain_input == list_pilihan_computer[2] or pemain_input == list_pilihan_computer[3] or pemain_input == list_pilihan_computer[4] or pemain_input == list_pilihan_computer[5] or pemain_input == list_pilihan_computer[6] or pemain_input == list_pilihan_computer[7] or pemain_input == list_pilihan_computer[8] or pemain_input == list_pilihan_player[0] or pemain_input == list_pilihan_player[1] or pemain_input == list_pilihan_player[2] or pemain_input == list_pilihan_player[3] or pemain_input == list_pilihan_player[4] or pemain_input == list_pilihan_player[5] or pemain_input == list_pilihan_player[6] or pemain_input == list_pilihan_player[7] or pemain_input == list_pilihan_player[8]):
                    print ("")
                    print ("------------------------------------")
                    print ("Pilihan Yang Anda Masukan Sudah Ada")
                    print ("Tolong Masukan Pilihan Lain!")
                    print ("------------------------------------")
                    print ("")
                    pemain_input = input("Masukan Pilihan Anda : ")
                    pemain_input = pemain_input.upper()

                list_pilihan_player[nomor_player] = pemain_input
                nomor_player += 1
                print ("")

                if pemain_input in papan_permainan:
                    papan_permainan[pemain_input] = " X "
                    pemain = 2            
                    break
                else:
                    print ("-------------------------")
                    print ("Masukan Pilihan Yang Ada!")
                    print ("-------------------------")
                    print ("")
                    petuntuk_game()
                    continue
            else:
                pilihan_computer = random.randint(0,8)
                computer_input = list_pilihan[pilihan_computer]

                while (computer_input == list_pilihan_player[0] or computer_input == list_pilihan_player[1] or computer_input == list_pilihan_player[2] or computer_input == list_pilihan_player[3] or computer_input == list_pilihan_player[4] or computer_input == list_pilihan_player[5] or computer_input == list_pilihan_player[6] or computer_input == list_pilihan_player[7] or computer_input == list_pilihan_player[8] or computer_input == list_pilihan_computer[0] or computer_input == list_pilihan_computer[1] or computer_input == list_pilihan_computer[2] or computer_input == list_pilihan_computer[3] or computer_input == list_pilihan_computer[4] or computer_input == list_pilihan_computer[5] or computer_input == list_pilihan_computer[6] or computer_input == list_pilihan_computer[7] or computer_input == list_pilihan_computer[8]):
                    pilihan_computer = random.randint(0,8)
                    computer_input = list_pilihan[pilihan_computer]

                list_pilihan_computer[nomor_computer] = computer_input

                print ("Computer Memilih : " + computer_input)
                print ("")
                papan_permainan[computer_input] = " O "

                nomor_computer += 1
                pemain = 1
                break

        game_jalan += 1

except KeyboardInterrupt:
    print ("")
    print ("")
    sys.exit("Program Dikeluarkan Oleh Pemain...")
