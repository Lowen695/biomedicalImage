import requests
from bs4 import BeautifulSoup as soup
import csv

source = requests.get('https://coreyms.com/').text
doc = soup(source,'html.parser')

csv_file = open('scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Link'])

for article in doc.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find(class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find(class_ = 'youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()