import pyinputplus as py

response=py.inputNum(limit=3,default='N/A')
response=py.inputNum(timeout=10,default='incorrect')

print(response)
