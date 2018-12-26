import settings

try:

    from urllib.parse import urlparse

except ImportError:

    from urlparse import urlparse

params_to_d = lambda params: {l[0]: l[1] for l in map(lambda j: j.split('='), urlparse(params).query.split('&'))}


