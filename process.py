from bs4 import BeautifulSoup as bs

import re

html = open("emoji.html").read()
soup = bs(html, "html.parser")
#print(soup.prettify())

out = open("emoji_list", "w")

tags = soup.find_all("td",{"title": re.compile('.: .*')})

for i in tags:
    #if i.string is not None:
    #print(i["title"])
    sp = i["title"].split(":")
    out.write(sp[0]+sp[1]+"\n")
    print(sp[0]+sp[1])

#print(tags[0].prettify())
