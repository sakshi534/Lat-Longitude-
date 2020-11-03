import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.lat-long.com/ListLocations-26-California-Beach.html' #TODO have to dynamically update the page
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.findAll('a'))

for i in range (8,32):
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    print(link)
    a="https://www.lat-long.com"
    link = a + link
    response = requests.get(link)
    print(link)
    soup1 = BeautifulSoup(response.text)
    for script in soup1(["script", "style"]):
        script.decompose()
    strips = list(soup1.stripped_strings)
    print("strips[0]", strips[0])
    print("strips[151]", strips[151])
    print("strips[152]", strips[152])
    ind=df.shape[0]+i
    df.loc[ind] = [strips[0],strips[151],strips[152]]
    print("i value", i)
    import time
    time.sleep(5)
print(df)

#TODO export the df
