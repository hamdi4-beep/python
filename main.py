from urllib.request import *
from html.parser import HTMLParser

url = 'https://pyautogui.readthedocs.io/en/latest/'
f = open('links.txt', 'w+')

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return

        for attr in attrs:
            key, value = attr
            f.write(f'{value}\n')

parser = Parser()

with urlopen(url) as response:
    buffer = response.read()
    parser.feed(buffer.decode())

f.close()