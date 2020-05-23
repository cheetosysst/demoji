from bs4 import BeautifulSoup as bs
import requests
import re
import emoji

html = requests.get("https://zh.wikipedia.org/wiki/繪文字")
soup = bs(html.text, "html.parser")
#print(soup.prettify())

out = open("emoji_list", "w")

tags = soup.find_all("td",{"title": re.compile('.: .*')})

for i in tags:
    #if i.string is not None:
    #print(i["title"])
    sp = i["title"].split(":")
    uni = sp[0].split("+")[1]
    out.write(chr(int(uni,16))+" "+sp[0]+sp[1]+"\n")
    print(chr(int(uni, 16)), sp[1])

#print(tags[0].prettify())
