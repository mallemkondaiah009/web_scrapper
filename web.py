import requests
from bs4 import BeautifulSoup
import csv

url="https://www.amazon.in/s?k=vivo+t2+5g+pro&adgrpid=152267697985&hvadid=671617185015&hvdev=c&hvlocphy=9147432&hvnetw=g&hvqmt=b&hvrand=15060892422453443355&hvtargid=kwd-2006888589100&hydadcr=24569_2265455&tag=googinhydr1-21&ref=pd_sl_3cd2410dll_b"

page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")

image=soup.findAll("div",class_="a-section aok-relative s-image-fixed-height")
print(image)