---
title: 'Scraping Pull Requests'
description: ''
publishDate: '1. October 2019'
author: 'Author'
heroImage: ''
alt: 'Astro'
layout: '../../layouts/BlogPost.astro'
---

Sometimes you may want to gather information from a webste and create a report of the gathered data. Extracting data from a web page is called web scraping.

I had an assingment to parse Pull Requests from Bitbucket and write the information to Excel.
For this we can utilize a couple of great Python libraries.

[Selenium][selenium] is a nifty browser automation library that can navigate to URLs, read information from the page, click links and much more.

Install the libs we will be using.

{% highlight shell %}
pip install selenium
pip install xlsxwriter
{% endhighlight %}

Basic setup requires importing a webdriver that can be specified to a browser of your choise.
It´s good to define the PullRequestScraper as a class and add methods that implement the desired logic.


{% highlight python %}
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import xlsxwriter

class PullRequestScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='~/Downloads/chromedriver_win32/chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

if __name__ == '__main__':
    scraper = PullRequestScraper()
{% endhighlight %}

We want to navigate to a page in Bitbucket that lists open Pull Requests. 

{% highlight python %}
    def get_open(self):
        self.driver.get('https://<domain>/stash/projects/<project>/repos/<repo>/pull-requests?state=OPEN')
{% endhighlight %}

Bitbucket will redirect to login page so we should implement a method for handling the login process.

First assert is for making sure we are on the correct page.

{% highlight python %}
    def login(self):
        assert "Log in - Bitbucket" in self.driver.title

        myusername = ""
        mypassword = ""

        username = self.driver.find_element_by_id("j_username")
        username.clear()
        username.send_keys(myusername)

        password = self.driver.find_element_by_name("j_password")
        password.clear()
        password.send_keys(mypassword)

        self.driver.find_element_by_id("submit").click()
{% endhighlight %}

Don´t forget to call your methods in the init phase.

{% highlight python %}
    scraper.get_open()
    scraper.login()
{% endhighlight %}

Next we need to parse the Pull Requests from the list.
XPATH is a utility that allows specifying an DOM tree element with a special syntax.

{% highlight python %}
    def parse_pull_requests(self):
        pull_requests_table = self.driver.find_element(By.XPATH,'//*[@id="pull-requests-content"]/div/div/table')
        pull_requests_titles = pull_requests_table.find_elements(By.XPATH,'//*[@class="pull-request-title"]')

        for title in pull_requests_titles:
            title = title.get_attribute('innerHTML')
{% endhighlight %}

Add the call for this method also.

{% highlight python %}
    scraper.parse_pull_requests()
{% endhighlight %}

OK so now we get a list of titles. 
The last part is to write it to Excel spreadsheet.
There are multiple libraries for this but let´s use [XLSXWriter][xlsxwriter].
Create an instance of a workbook and name it.

{% highlight python %}
    workbook = xlsxwriter.Workbook('pull_requests.xlsx')
    worksheet = workbook.add_worksheet("Open")
{% endhighlight %}

Now we can plug in the worksheet to our parse method.

{% highlight python %}
    def parse_pull_requests(worksheet):
{% endhighlight %}

Calling the write method of the worksheet will insert each title in the spreadsheet while we loop through the list. Provide the row ID as variable i.

{% highlight python %}
    i = 0
    for title in pull_requests_titles:
        # row, column, item
        worksheet.write(i, 0, title)
        i += 1
{% endhighlight %}

In the end you should close the workbook.

{% highlight python %}
    workbook.close()
{% endhighlight %}

Also implement the quit() method andd call it to stop the scraper.
{% highlight python %}
    def quit(self):
        self.driver.close()
{% endhighlight %}

{% highlight python %}
    scraper.quit()
{% endhighlight %}


Finally save the script with name PullRequestScraper.py and launch with command:

{% highlight shell %}
python PullRequestScraper.py
{% endhighlight %}

Find the full code on this [Gist][gist] 

[selenium]:      https://www.seleniumhq.org/
[xlsxwriter]:      https://pypi.org/project/XlsxWriter/
[gist]:      https://gist.github.com/jounile/d146fb7836cc92fe20b1a3f4deaeadaa
