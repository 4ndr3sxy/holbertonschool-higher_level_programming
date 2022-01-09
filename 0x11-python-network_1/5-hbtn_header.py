#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    for header, value in r.__dict__['headers'].items():
        if header == "X-Request-Id":
            print(value)
            break
