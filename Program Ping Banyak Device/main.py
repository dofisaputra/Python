# author : dofisaputra
# program untuk ping banyak ip

import os

ip_address = []

ulang = "Y"

while ulang == "Y":
    input_ip = input("\nMasukan IP Address : ")
    ip_address.append(input_ip)

    tanya = "Y"
    while tanya == "Y":
        input_tanya = input("\nMasukan IP Lagi? (y/n) : ")
        input_tanya = input_tanya.upper()
        if input_tanya == "Y":
            tanya = "Y"
            break
        elif input_tanya == "N":
            tanya = "N"
            ulang = "N"
        else:
            print("\nMasukan y/n!")
            continue

print ("\nMulai PING... \n")

for ip in ip_address:
    ping = os.system("ping -c 4 {}".format(ip))
    if ping == 0:
        print("\n\n{} Up! \n\n".format(ip))
    else:
        print("\n\n{} Down! \n\n".format(ip))
    