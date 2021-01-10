from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas

try:

    titles = []
    channels = []
    viewss = []

    print("\nTunggu Beberapa Saat...")

    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    wait = WebDriverWait(driver, 10)

    trending = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Trending']")))
    trending.click()

    all_videos = wait.until(EC.presence_of_element_located((By.ID, 'grid-container')))
    videos = all_videos.find_elements_by_id('dismissable')

    for video in videos:
        title = video.find_element_by_id('video-title').text
        channel = video.find_element_by_id('text').text
        views = video.find_element_by_css_selector("span[class='style-scope ytd-video-meta-block']").text

        titles.append(title)
        channels.append(channel)
        viewss.append(views)
        
    videos_dict = {"Judul Video": titles, "Channel Youtube": channels, "Views": viewss}

    videos_df = pandas.DataFrame(videos_dict)

    videos_df.to_csv("Selenium Video Trending Youtube.csv")

except:
    print("\nGagal, Silahkan Ulang\n")
    driver.quit()

finally:
    print("\nSelesai, file : Selenium Video Trending Youtube.csv\n")
    driver.quit()