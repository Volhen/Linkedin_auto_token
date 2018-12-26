from urllib import parse

import requests

import json

import settings


def authorization_url():

    values = {'response_type': 'code',
              'client_id': settings.API_KEY,
              'redirect_uri': settings.RETURN_URL,
              'state': settings.STATE,
              'scope': 'r_basicprofile'}

    data = parse.urlencode(values)

    URL = settings.URL_FOR_OAUTH + str(data)

    return URL


def authorization_code(CODE):

    proxies = {"http": "http://{}:{}".format(settings.HOST_PROXY,str(settings.PORT_PROXY)),
               "https": "http://{}:{}".format(settings.HOST_PROXY,str(settings.PORT_PROXY))}

    values = {'grant_type': 'authorization_code',
              'code': CODE,
              'redirect_uri': settings.RETURN_URL,
              'client_id': settings.API_KEY,
              'client_secret': settings.API_SECRET}

    URL = settings.URL_FOR_TOKEN

    r = requests.post(URL, data=values,json=None, proxies=proxies)

    str_token = json.loads(r.text)

    return str_token['access_token']


# def authorization_code(CODE):

#     values = {'grant_type': 'authorization_code',
#               'code': CODE,
#               'redirect_uri': settings.RETURN_URL,
#               'client_id': settings.API_KEY,
#               'client_secret': settings.API_SECRET}

#     data = parse.urlencode(values)

#     URL = str(data)

#     # CURL = 'curl -x {}:{} {} -d "{}"'.format(settings.HOST_PROXY, settings.PORT_PROXY, settings.URL_FOR_TOKEN, URL)
#     CURL = '{} "{}"'.format(settings.URL_FOR_TOKEN, URL)

#     return CURL
