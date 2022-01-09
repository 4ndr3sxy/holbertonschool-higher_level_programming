#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        # if json is not empty and json correct:
            # print("[{}] <{}>".format(id, name))
        # elif json incorrect:
            # print("Not a valid JSON")
        # else:
            # print("No result")
    else:
        print("No result")
    # data = urllib.parse.urlencode({"email": sys.argv[2]})
    # data = data.encode('ascii')
    # url = sys.argv[1]
    # with urllib.request.urlopen(url, data) as response:
    #     print(response)


