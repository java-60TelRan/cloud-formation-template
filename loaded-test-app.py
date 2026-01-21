import requests
import concurrent.futures

URL = "https://telran.org/health"
N = 200  # try 200, then 500

def call(_):
    r = requests.get(URL, timeout=5)
    return r.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
    results = list(ex.map(call, range(N)))

print("done, sample:", results[:10])
