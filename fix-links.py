#!/usr/bin/python
from bs4 import BeautifulSoup

files = ["dist/index.html", "dist/contact.html"]

for file in files:
    
    # Read html file
    f = open(file, 'r')
    html = f.read()
    soup = BeautifulSoup(html, "html.parser")

    for a_tag in soup.find_all('a'):
        old_href = a_tag['href']
        if not str(old_href).startswith("https://"):
            new_href = old_href + ".html"
            a_tag['href'] = a_tag['href'].replace(old_href, new_href)

    soup = soup.prettify()
    print(soup)

    # Write modified html to file
    f = open(file, 'w')
    f.write(soup)