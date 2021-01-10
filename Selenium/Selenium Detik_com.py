from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas

kumpulan_judul_berita = []

driver = webdriver.Chrome()
driver.get("https://www.detik.com/")

try:   
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "query"))
    )

    pencarian = driver.find_element(By.NAME, "query")
    pencarian.send_keys("pesawat")
    pencarian.send_keys(Keys.RETURN)

    nomor_halaman = 1
    
    while nomor_halaman <= 100:

        print("\nScraping Halaman", nomor_halaman)

        kumpulan_berita = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='list media_rows list-berita']")))
        berita = kumpulan_berita.find_elements_by_tag_name('article')

        for x in berita:
            wait = WebDriverWait(x, 10)
            
            judul_berita = wait.until(lambda x: x.find_element_by_tag_name("h2"))
            kumpulan_judul_berita.append(judul_berita.text)

        nomor_halaman += 1
        halaman = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, str(nomor_halaman)))).click()

    dict_berita = {"Judul Berita": kumpulan_judul_berita}

    df_berita = pandas.DataFrame(dict_berita)

    df_berita.to_csv("Selenium Detik_com (keyword pesawat).csv")

finally:
    print("\nSelesai....\n")
    driver.quit()

