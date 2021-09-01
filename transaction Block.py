# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:22:04 2018

@author: jacques
"""
import hashlib
import pickle
top_block={
        '     transaction using my first block I wrote                ' :[
                {
                 '   from' : '       A            '  ,
                 '   to' :'   B           '  ,
                 '   amount': 100
                 },
                 {'  from  ' :'  B   '  ,
                 '   to   ' :'  C   '  ,
                 '    amount   ': 1000
                 },
                  
                 {'  from   ' :'C',
                 '    to   ' :'D',
                 '   amount   ': 10,
                 'message' : '           Im making flippin crypto! Me jacques lavoie           '
                 },
                  
                 ],
  'last_block' : m.digest(),
  'nonce':2
  }
pickle.dumps(top_block)

m=hashlib.sha3_256()
m.update(pickle.dumps(block))
m.digest()
m.hexdigest()

print(block)
print(m.hexdigest())
print(top_block)
