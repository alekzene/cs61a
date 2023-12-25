from json import loads
# json loads gets a string from a json file and converts it to a Python dictionary

from urllib.request import urlopen
# urllib.request urlopen contains methods that help open URLs

# FIXME line seems to have no effect
loads(urlopen('https://howsmyssl.com/a/check').read().decode('UTF-8'))['tls_version']
