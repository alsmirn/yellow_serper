#!/usr/bin/env python
__author__ = 'Alexey Smirnov <alsmirn@gmail.com>'

import urllib

import requests


class YellowSerper():
    """YellowSerper is a class for working with Yandex.XML service.
    More documentation here:
        http://api.yandex.ru/xml/doc/dg/concepts/get-request.xml
    """

    def __init__(self, credentials):
        self.credentials = credentials
        self.request_url = 'http://xmlsearch.yandex.ru/xmlsearch'

    def get(self, query, **kwargs):
        params = {'query': query}
        params.update(self.credentials)
        params_allowed = (
            'lr', 'l10n', 'sortby', 'filter', 'maxpassages', 'groupby', 'page'
        )
        if kwargs:
            params.update(
                dict((k, v) for k, v in kwargs.items() if k in params_allowed)
            )
        link = "%s/%s" % (self.request_url, urllib.urlencode(params))
        response = requests.get(link)

        return response.text


if __name__ == '__main__':
    credentials = {
        'user': 'USER HERE',
        'key': 'KEY HERE'
    }
    ys = YellowSerper(credentials)
    print ys.get('Yandex Search API bro? Yandex.XML.', page=1)
