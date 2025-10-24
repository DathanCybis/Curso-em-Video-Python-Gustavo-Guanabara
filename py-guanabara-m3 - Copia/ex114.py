#crie um programa em py que teste se o site "Pudim" está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print("O site pudim não acessível!")
else:
    print("O site pudim está acessível!")
#    print(site.read())
