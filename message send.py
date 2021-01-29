import requests
#import random
mobno=input("enter no")
msg="this is message"
res=requests.post('https://textbelt.com/text',{'phone':mobno,'message':msg,'key':'textbelt'})
#use +91
result=res.json()
print(result)
