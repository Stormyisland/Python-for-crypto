# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:08:03 2018

@author: jacques
"""
import hashlib

m=hashlib.sha3_256()
m.update(b'hello world')
m.digest()


n=hashlib.sha256()
n.update(b'hello world you big buitiful babe')
n.digest()


print (m.hexdigest())
print (n.hexdigest()) 