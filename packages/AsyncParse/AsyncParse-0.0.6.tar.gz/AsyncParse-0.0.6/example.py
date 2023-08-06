from AsyncParse.main import Fetch


REQUESTS_PER_SEC = 20 # Number of requests per second 
SHOW_RESULTS = True 
data = [] #how to store data. Note! It has to be compatible with parse function you will pass in

fetcher = Fetch(REQUESTS_PER_SEC, data, SHOW_RESULTS)

URLS = ['SOME URLS'] 

def parse_func(parser_instance, response):
    """DO SOME PARSING HERE AND RETURN WHAT YOU WANT"""
    """UPDATE parser_instance.data - this is where your data is stored""" 
    return response

fetcher(URLS, "GET", parse_func)
fetcher.data # -> output your data