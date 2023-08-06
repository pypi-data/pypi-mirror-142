from AsyncParse.main import Fetch


REQUESTS_PER_SEC = 20 # Number of requests per second 
SHOW_RESULTS = True 
data = [] #how to store data. Note! It has to be compatible with parse function you will pass in

fetcher = Fetch(REQUESTS_PER_SEC, data, SHOW_RESULTS)

URLS = ['https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8']*10

def parse_func(response):
    return response

fetcher(URLS, "GET", parse_func)
print(fetcher.data) # -> output your data
print(fetcher) # -> check how much time was taken to execute