from urllib.request import Request, urlopen
from html.parser import HTMLParser

f = open('images.txt', 'w+')
URL = 'https://en.wikipedia.org/wiki/PlayStation_4'

class Parser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

    def handle_startendtag(self, tag, attrs):
        if tag != 'img':
            return
        
        for key, value in attrs:
            if not value.startswith('/'):
                return
            
            f.write(f'https:{value}\n')

        f.write('\n')

parser = Parser()

with urlopen(Request(URL)) as response:
    data = response.read()
    parser.feed(data.decode())

f.close()