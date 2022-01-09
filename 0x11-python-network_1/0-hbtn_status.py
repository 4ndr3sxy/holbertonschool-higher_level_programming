#!/usr/bin/python3
""" Get status in https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}".format(type(html), html))
        print("\t- utf8 content: {}".format(html.decode('UTF-8')))
