PyFrx
=====

A package to help convert currencies.


Details
-------

Simply, this package relies on current forex market rate to check conversion.


Package Usage
-------------

import pyfrx

\# show supported currencies
pyfrx.supported_currencies()

\# to just get the rate 
pyfrx.rate('gbp','pkr')

\# to get amount conversion
pyfrx.convert('gbp', 'pkr', 10)
