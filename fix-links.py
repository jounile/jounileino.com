#!/usr/bin/python
from bs4 import BeautifulSoup

"""
Before using this script run the following command: 
$ npm run build

Hosting a static website in AWS S3 requires that names of the accessed object is exactly the one that a link points to.
Astro creates a /dist directory with all the HTML pages. Astro creates also routes that have no .html extension.
For example a link in Astro site points to /contact and the /dist directory contains a file named contact.html.
In order to access that HTML page in a S3 bucket the link needs to point to a path with the .html extension.
This script loops through the specified HTML files and adds the .html extension to links.

for example this 
<a href="/contact">Link</a>
becomes this
<a href="/contact.html">Link</a>

This script will update the links and write the prettified html content into each HTML file.
After this script has executed you can sync the /dist directory content to S3 bucket.
See the project README
"""

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