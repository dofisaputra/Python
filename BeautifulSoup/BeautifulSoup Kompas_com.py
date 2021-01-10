from bs4 import BeautifulSoup
import requests
import pandas

kumpulan_judul_berita = []
kumpulan_tanggal_berita = []

index_halaman = 1

while index_halaman <= 10:
    halaman = requests.get("https://indeks.kompas.com/?page=" + str(index_halaman))
    soup = BeautifulSoup(halaman.content, "lxml")
    
    kumpulan_berita = soup.find_all("div", "article__list clearfix")

    for berita in kumpulan_berita:
        judul_berita = berita.find("a", "article__link").text
        tanggal_berita = berita.find("div", "article__date").text

        kumpulan_judul_berita.append(judul_berita)
        kumpulan_tanggal_berita.append(tanggal_berita)

    print("Scrap Halaman-" + str(index_halaman))
    index_halaman += 1   

dict_berita = {"Judul Berita": kumpulan_judul_berita, "Tanggal Berita": kumpulan_tanggal_berita}

df_berita = pandas.DataFrame(dict_berita)

df_berita.to_csv("BeautifulSoup Kompas_com.csv")