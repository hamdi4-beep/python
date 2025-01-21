from urllib.request import Request, urlopen
from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.isWithinSelectedTag = False
    
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == 'class' and value == 'sphinxsidebarwrapper':
                self.isWithinSelectedTag = True

    def handle_data(self, data):
        if self.isWithinSelectedTag and data.strip():
            print(data)

parser = Parser()

with urlopen('https://docs.python.org/3/library/html.parser.html') as response:
    data = response.read()
    parser.feed(data.decode())