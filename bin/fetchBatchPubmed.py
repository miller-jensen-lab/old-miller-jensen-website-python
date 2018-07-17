#!/usr/bin/env python
""" Fetches pubmed records
"""
import sys
from urllib.parse import urlencode
from urllib.request import urlopen
import re
import json


def usage():
    print("{0}: Takes a list of Pubmed IDs and returns in requested format".format(
        sys.argv[0]))
    print("Usage: %s RETURN_TYPE FORMAT \"SEARCH\"".format(sys.argv[0]))
    print("RETURN_TYPE = [uilist, abstract, citation, text]")
    print("FORMAT = [xml, text, html, asn.1]")
    print("SEARCH = pubmed search terms")


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
    urlParams = urlencode(searchParams)
    f = urlopen("%s%s" % (esearchUrl, urlParams)).read().decode('utf-8')

    Count = ""
    QueryKey = ""
    WebEnv = ""
    for line in f.splitlines():

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

    Count = int(Count)
    QueryKey = int(QueryKey)
    return (Count, QueryKey, WebEnv)


def retrieveWithWebEnv(Count, QueryKey, WebEnv, retmode, rettype):
    retmax = 500
    esearchUrl = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"
    searchParams = {
        "db": "pmc",
        "WebEnv": WebEnv,
        "query_key": QueryKey,
        "retmax": retmax,
        "retmode": retmode,
        "rettype": rettype,
        "retstart": 0
    }

    for retstart in range(0, Count, retmax):
        searchParams["retstart"] = retstart
        urlParams = urlencode(searchParams)
        f = urlopen("%s%s" % (esearchUrl, urlParams))
        esummary = json.loads(f.read().decode('utf-8'))
        print(tranform(esummary))


def get_doi(articleids):
    dois = [x['value'] for x in articleids if x['idtype'] == 'doi']
    if len(dois) > 0:
        return dois[0]
    return None


def tranform(esummary):
    """ Transforms esummary object into the format we want
        for the Miller-Jensen website
    """
    uids = [uid for uid in esummary['result'].keys() if uid != 'uids']
    output = []
    for uid in sorted(uids):
        record = esummary['result'][uid]
        authors = ", ".join(au['name'] for au in record['authors'])
        o = {
            'authors': authors,
            'title': record['title'],
            'pmid': uid,
            'volume': record['volume'],
            'issue': record['issue'],
            'year': int(record['pubdate'].split()[0]),
            'pages': record['pages'],
            'journal': record['source'],
            'doi': get_doi(record['articleids'])
        }
        output.append(o)

    return output


def main():
    if len(sys.argv) is not 2:
        usage()
        sys.exit()

    rettype = 'abstract'
    retmode = 'json'
    query = sys.argv[1]

    (Count, QueryKey, WebEnv) = searchPubmed(query)
    retrieveWithWebEnv(Count, QueryKey, WebEnv, retmode, rettype)


if __name__ == "__main__":
    sys.exit(main())
