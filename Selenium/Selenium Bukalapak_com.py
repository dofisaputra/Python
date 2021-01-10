from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
import time

kumpulan_judul_produk = []
kumpulan_harga_produk = []
kumpulan_link_produk = []

driver = webdriver.Chrome()
driver.get("https://bukalapak.com/")

try:
    keyword = "xiaomi" #bisa diganti sesuai keinginan :D
    wait = WebDriverWait(driver, 20)

    search = wait.until(lambda driver: driver.find_element_by_id("v-omnisearch__input"))
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)

    nomor_halaman = 1

    while nomor_halaman <= 5: # jumlah halaman --> bisa di ganti seusai keinginan
        print("\nScraping Halaman-" + str(nomor_halaman))
        time.sleep(3)

        kumpulan_produk = wait.until(lambda driver: driver.find_element_by_css_selector("div[class='bl-flex-container flex-wrap is-gutter-16']"))
        produk = WebDriverWait(kumpulan_produk, 20).until(lambda kumpulan_produk: kumpulan_produk.find_elements_by_css_selector("div[class='bl-flex-item mb-8']"))

        for x in produk:
            wait_produk = WebDriverWait(x, 20)

            title = wait_produk.until(lambda x: x.find_element_by_class_name("bl-product-card__description-name"))
            price = wait_produk.until(lambda x: x.find_element_by_xpath("//*[@id='product-explorer-container']/div/div/div[2]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/p"))
            link = wait_produk.until(lambda x: x.find_element_by_tag_name("a")).get_attribute("href")

            kumpulan_judul_produk.append(title.text)
            kumpulan_harga_produk.append(price.text)
            kumpulan_link_produk.append(link)
            
        nomor_halaman += 1
        if nomor_halaman == 5:
            time.sleep(3)
            driver.back()
            halaman = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, str(nomor_halaman)))).click()
        else:
            halaman = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, str(nomor_halaman)))).click()

    dict_produk = {"Nama Produk": kumpulan_judul_produk, "Harga": kumpulan_harga_produk, "Link Pembelian": kumpulan_link_produk}
    df_produk = pandas.DataFrame(dict_produk)

    df_produk.to_csv("Selenium Bukalapak_com (keyword xiaomi).csv")

finally:
    print("\nSelesai...\n")
    driver.quit()