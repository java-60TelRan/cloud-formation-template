import requests
import time

URL = "https://tel-ran.org/greeting"

i = 1
for i in range(50):
    try:
        r = requests.get(URL, timeout=5)
        print(f"{i:04d}  {r.status_code}")
    except Exception as e:
        print(f"{i:04d}  ERROR {e}")
    i += 1
    time.sleep(1)
