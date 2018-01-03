
# coding: utf-8

# In[1]:

#Dependencies

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import time


# In[2]:

#URL to the page to be scraped.

url = 'https://mars.nasa.gov/news/'


# In[3]:

#Retrieve the page with the requests module.

response = requests.get(url)


# In[4]:

# Create BeautifulSoup object; parse with 'html.parser'.

soup = BeautifulSoup(response.text, 'html.parser')

#Print results.
print(soup.prettify())


# In[5]:

results_title = soup.find('div',class_='content_title').text
results_title


# In[6]:

news_title = str(results_title)
print(news_title)


# In[7]:

result_p = soup.find('div', class_='rollover_description_inner').text
result_p


# In[8]:

news_p = str(result_p)
print(news_p)


# In[9]:

# Use Splinter to scrape the NASA JPL page.

browser = Browser('firefox')
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html,'html.parser')
image = soup.body.find('img', class_='fancybox-image')
image


# In[10]:

featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19952_ip.jpg'


# In[11]:

#Scrape the NASA Twitter feed.

url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
results = soup.body.find_all('p')[2].text
results


# In[12]:

mars_weather = str(results)
print(mars_weather)


# In[13]:

#Use Pandas to scrape the Mars facts website.

url = 'https://space-facts.com/mars/'
mars_table = pd.read_html(url)
mars_table


# In[14]:

mars_table_df = mars_table[0]
mars_table_df.columns = ['Fact','Data']
mars_table_df


# In[15]:

table_html = mars_table_df.to_html(header=True, index=False)
print(table_html)


# In[16]:

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html,'html.parser')
hemispheres = soup.find('div',class_='collapsible results')

results = hemispheres.find_all('a')
print(results)


# In[17]:

hemisphere_list = []

for result in results:
    title = result.h3.text
    link = 'https://astrogeology.usgs.gov' + result['href']
    print(title,link)    
    browser.visit(link)
    time.sleep(5)
    image_html = browser.html
    soup = BeautifulSoup(image_html,'html.parser')
    soup_image = soup.find('div', class_='downloads').find('li').a['href']
    print(soup_image)
    mars_images = {'title':title, 'img_url':soup_image}
    hemisphere_list.append(mars_images)


# In[18]:

print(hemisphere_list)


# In[ ]:



