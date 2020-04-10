#!/usr/bin/env python
# coded by ghosthub (b@b@y)
# works with: bit.ly, goo.gl, t.co, ow.ly, tinyurl.com and probably many more

import sys
import os
import getopt
import requests

def extract_tinyurl(url):
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    print(resp.url)

def prepend_http(url):
    return  "http://" + url

def starts_with_http(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True

def usage(app):
    app = os.path.basename(app)
    sys.stderr.write("usage: %s [-h] [-t URL]\n" % (app))
    sys.exit(1)

def main(args):
    try:
        opts, largs = getopt.getopt(args[1:], "ht:")
    except getopt.GetoptError as err:
        print(str(err))
        print(err)
        usage(args[0])

    if len(args) <= 1:
        usage(args[0])

    for o, a in opts:
        if o == "-h":
            usage(args[0])
        elif o == "-t":
            if starts_with_http(a):
                extract_tinyurl(a)
            else:
                extract_tinyurl(prepend_http(a))
        else:
            usage(args[0])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

    
