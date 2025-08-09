import requests, time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)

        print(f'{func.__name__} took {time.perf_counter() - start} seconds\n')

        return ret

    return wrapper

@measure_time
def fetch_url(session, url):
    try:
        with session.get(url, stream=True) as response:
            response.raise_for_status()
            total = 0

            for chunk in response.iter_content(chunk_size=8192):
                total += len(chunk)

            print(f'Fetched {total} bytes from {url}')
            return total
    except Exception as ex:
        print(f'Something went wrong fetching {url}: {ex}')

def main():
    urls = [
        'https://python.org',
        'http/github',
        'https://javascript.info'
    ]

    with requests.Session() as session:
        print([fetch_url(session, url) for url in urls])

if __name__ == '__main__':
    main()