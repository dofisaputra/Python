import requests
from bs4 import BeautifulSoup
import pandas

try:

    titles = []
    times = []

    page = requests.get("https://www.tribunnews.com/news")
    soup = BeautifulSoup(page.content, "lxml")

    news = soup.find_all('li', 'p1520 art-list pos_rel')

    for x in news:
        title = x.find('a', 'f20 ln24 fbo txt-oev-2').text.strip()
        time = x.find('time', 'foot timeago').text

        titles.append(title)
        times.append(time)

    news_dict = {'Judul Berita': titles, 'Waktu Diunggah': times}
    news_df = pandas.DataFrame(news_dict)

    result = 'BeautifulSoup Tribun_com (Berita Terbaru).csv'
    news_df.to_csv(result)

except:
    print("\nScraping Gagal...\n")

finally:
    print("\nScraping Berhasil, Nama File : " + result + "\n")