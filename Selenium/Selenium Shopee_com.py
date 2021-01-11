from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
import time

try:

    titles = []
    original_prices = []
    discount_prices = []
    solds = []

    print("\nTunggu Sebentar")

    driver = webdriver.Chrome()
    driver.get("https://shopee.co.id/")

    wait = WebDriverWait(driver, 10)

    popUp = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='shopee-popup__close-btn']"))).click()

    flashSale = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='shopee-button-no-outline']"))).click()

    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 6000);")

    time.sleep(10)

    allProduct = wait.until(lambda driver: driver.find_element_by_css_selector("div[class='flash-sale-items']"))

    product = WebDriverWait(allProduct, 10).until(lambda allProduct: allProduct.find_elements_by_css_selector("div[class='flash-sale-item-card flash-sale-item-card--landing-page flash-sale-item-card--ID']"))

    for x in product:
        wait_product = WebDriverWait(x, 10)

        title = wait_product.until(lambda x: x.find_element_by_class_name("flash-sale-item-card__item-name")).text
        original_price = wait_product.until(lambda x: x.find_element_by_class_name("flash-sale-item-card__original-price")).text
        discount_price = wait_product.until(lambda x: x.find_element_by_css_selector("div[class='flash-sale-item-card__current-price flash-sale-item-card__current-price--landing-page']")).text
        sold = wait_product.until(lambda x: x.find_element_by_class_name("flash-sale-progress-bar__text")).text

        titles.append(title)
        original_prices.append(original_price)
        discount_prices.append(discount_price)
        solds.append(sold)

    dict_product = {"Nama Produk": titles, "Harga Awal": original_prices, "Harga Discount": discount_prices, "Banyaknya Terjual": solds}

    df_product = pandas.DataFrame(dict_product)

    df_product.to_csv("Selenium Flash Sale Shopee.csv")

finally:
    print("\nSelesai, file : Selenium Flash Sale Shopee.csv\n")
    driver.quit()