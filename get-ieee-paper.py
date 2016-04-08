#!/usr/bin/env python
import sys
import re
import urlparse
import os

def get_arnumber(strurl):
    # try url first
    parsed = urlparse.urlparse(strurl)
    params = urlparse.parse_qs(parsed.query)

    if "arnumber" in params:
        return str(params["arnumber"][0])

    # maybe strurl is a pure number
    num_result = re.match(r"\b(\d+)\b", strurl)
    if num_result:
        return str(num_result.group(0))

    # fail otherwise
    return None

def main():
    # print help
    if len(sys.argv) <= 1:
        print "usage: %s <ieeeurl|arnumber>" % sys.argv[0]
        sys.exit()

    # determine article number
    arnumber = get_arnumber(sys.argv[1])
    if not arnumber:
        print "could not determine arnumber"
        sys.exit(1)

    # form wget url
    url = "http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?arnumber=%s" % arnumber
    filename = "%s.pdf" % arnumber

    # download over ssh proxy
    # TODO: replace credentials here, and set up SSH keys
    cmd = "ssh username@remotehost 'wget -q -O - \"%s\"' > %s.pdf" % (url, arnumber)
    print "Executing command"
    print ">", cmd
    os.system(cmd)

if __name__ == '__main__':
    main()
