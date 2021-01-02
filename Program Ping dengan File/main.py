''' 
    author : dofisaputra
    program ping banyak device dengan file
'''

import os

while True:
    try:
        input_file = input("\nMasukan File IP Adress : ")
        file_ip = open(input_file)
        read_file_ip = file_ip.readlines()
        file_ip.close()
        break
    except IOError:
        print ("\nNama File Yang Anda Masukan Tidak Ada!")
        print ("Coba Masukan Lagi!")
        continue

print ("\nMulai PING...\n")

for x in read_file_ip:
    ping = os.system("ping -c 4 {}".format(x))
    if ping == 0:
        print ("\n{}this Up!\n".format(x))
    else:
        print ("\n{}this Down!\n".format(x))

print ("Finish :D\n")