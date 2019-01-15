# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
r=requests.get('https://apiv2.bitcoinaverage.com/weighting/exchanges')
 
print(r.text)