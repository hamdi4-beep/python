from urllib.request import urlopen

with urlopen('http://api.github.com/users/hamdi4-beep') as response:
    for header in response.getheaders():
        key, value = header

        if key == 'Last-Modified':
            print(header)