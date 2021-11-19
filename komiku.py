from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import Request
from urllib.parse import urljoin
import time
import threading

headers = {'User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}

def get_url(url):
    try:
        req = Request(url=url, headers=headers)
        web = urlopen(req)
    except HTTPError as e:
        print(e)
    return BeautifulSoup(web.read(), 'html.parser')

def main(url):
    bs = get_url(url)
    links = bs.find('tbody', class_='_3Rsjq')
    for link in links.find_all('a'):
        print(urljoin(url, link.attrs['href']))

if __name__ == '__main__':
    threads = []
    x = input('url> ')
    thread = threading.Thread(target=main, args=(x,))
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()
