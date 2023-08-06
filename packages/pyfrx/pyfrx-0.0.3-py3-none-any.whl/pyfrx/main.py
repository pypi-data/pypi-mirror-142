#!/usr/bin/python

import sys
import getopt
import requests as r
from bs4 import BeautifulSoup as bs
from .supported_currencies import _SUPPORTED_CURRENCIES as SC

#https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=PKR
_u = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From={}&To={}'

def rate(from_curr, to_curr):
    res = r.get(_u.format(from_curr.upper(), to_curr.upper()))
    parsed = bs(res.content, 'html.parser')
    el = parsed.find('span', attrs={'class': 'faded-digits'})
    return float(el.parent.text.split()[0].replace(',',''))

def convert(from_curr, to_curr, amount):
    print( from_curr, to_curr, amount )
    r = rate(from_curr, to_curr)
    c = amount * r
    return c

def show_help():
    print('Usage: pyfrx <from_currency> <to_currency> [amount]')
    print('Example Output: {}'.format(rate('pkr', 'syp')))
    
def show_currencies():
    print('CURRENCIES')
    print('==========')

    for k,v in SC.items():
        print('\033[1m{}\033[0m {}'.format(v.upper(), k.upper()))

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'ch',['currencies', 'help'])
    for opt in opts:
        if opt[0] in ['-h', '--help']:
            show_help()
            sys.exit(0)
        elif opt[0] in ['-c', '--currencies']:
            show_currencies()
            sys.exit(0)

    nargs = len(args)
    if nargs < 2 or nargs > 3:
        raise Exception('Please check usage.')

    if nargs == 2:
        ans = rate(args[0], args[1])
    elif nargs == 3:
        ans = convert(args[0], args[1], float(args[2]))

    print('\033[1mRESULT\033[0m {} {}'.format(ans, args[1].upper()))
