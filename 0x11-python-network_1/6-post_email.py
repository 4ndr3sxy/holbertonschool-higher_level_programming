#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=payload)
    # data = urllib.parse.urlencode({"email": sys.argv[2]})
    # data = data.encode('ascii')
    # url = sys.argv[1]
    # with urllib.request.urlopen(url, data) as response:
    #     print(response)


