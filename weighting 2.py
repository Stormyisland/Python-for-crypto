# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:44:33 2018

@author: jacques
"""

import requests
r=requests.get('https://apiv2.bitcoinaverage.com/weighting/exchanges')
 
print(r.text)