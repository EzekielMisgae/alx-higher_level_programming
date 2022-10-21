#!/usr/bin/python3
"""Takes in a URL, sends request to URL & displays the value of the
X-request-Id variable found in the header of the response"""

if__name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
