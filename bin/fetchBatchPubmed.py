#!/usr/bin/env python
""" Fetches pubmed records
"""
import sys
import urllib
import re


def usage():
    print "%s: Takes a list of Pubmed IDs and returns in requested format" \
        % (sys.argv[0])
    print "Usage: %s RETURN_TYPE FORMAT \"SEARCH\"" % (sys.argv[0])
    print "RETURN_TYPE = [uilist, abstract, citation, medline]"
    print "FORMAT = [xml, text, html, asn.1]"
    print "SEARCH = pubmed search terms"


def searchPubmed(query):
    CountRegex = re.compile("<Count>(?P<Count>\d+)</Count>")
    QueryKeyRegex = re.compile("<QueryKey>(?P<QueryKey>\d+)</QueryKey>")
    WebEnvRegex = re.compile("<WebEnv>(?P<WebEnv>\S+)</WebEnv>")

    esearchUrl = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
    searchParams = {
        "db": "pubmed",
        "term": query,
        "usehistory": "y"
        }
    urlParams = urllib.urlencode(searchParams)
    f = urllib.urlopen("%s%s" % (esearchUrl, urlParams))

    Count = ""
    QueryKey = ""
    WebEnv = ""
    for line in f:

        match = CountRegex.search(line)
        if match is not None:
            Count = match.group(1)
        match = QueryKeyRegex.search(line)
        if match is not None:
            QueryKey = match.group(1)
        match = WebEnvRegex.search(line)
        if match is not None:
            WebEnv = match.group(1)

        if Count is not "" and QueryKey is not "" and WebEnv is not "":
            break

    f.close()

    Count = int(Count)
    QueryKey = int(QueryKey)
    return (Count, QueryKey, WebEnv)


def retrieveWithWebEnv(Count, QueryKey, WebEnv, retmode, rettype):
    retmax = 500
    esearchUrl = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
    searchParams = {
        "db": "pubmed",
        "WebEnv": WebEnv,
        "query_key": QueryKey,
        "retmax": retmax,
        "retmode": retmode,
        "rettype": rettype,
        "retstart": 0
        }

    for retstart in range(0, Count, retmax):
        searchParams["retstart"] = retstart
        urlParams = urllib.urlencode(searchParams)
        f = urllib.urlopen("%s%s" % (esearchUrl, urlParams))
        print f.read()
        f.close()


def main():
    if len(sys.argv) is not 4:
        usage()
        sys.exit()

    rettype = sys.argv[1]
    retmode = sys.argv[2]
    query = sys.argv[3]

    (Count, QueryKey, WebEnv) = searchPubmed(query)
    retrieveWithWebEnv(Count, QueryKey, WebEnv, retmode, rettype)


if __name__ == "__main__":
    sys.exit(main())
