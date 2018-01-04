
#Dependencies

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import time
    
#Init Browser

def init_browser():
    return Browser("firefox",headless=False)


def scrape():

    browser = init_browser()
    mission_to_mars = {}

    #Scrape the NASA Mars news site.
    mars_news_site = 'https://mars.nasa.gov/news/'
    response = requests.get(mars_news_site)
    browser.visit(mars_news_site)

    #Create BeautifulSoup object; parse with 'html.parser'.

    soup = BeautifulSoup(response.text, 'html.parser')

    #Print results.
    #print(soup_mars.prettify())
    #Append Mars news headline and paragraph to the dictionary.
    title = soup.find('div',class_='content_title').text

    #Append Mars news headline to the dictionary.
    mission_to_mars['Latest Mars News'] = title
    #news_title = str(results_title)
    #print(news_title)

    paragraph = soup.find('div', class_='rollover_description_inner').text

    #Append Mars news headline to the dictionary.
    mission_to_mars["Article"] = paragraph
    #news_p = str(result_p)
    #print(news_p)


# Use Splinter to scrape the NASA JPL page.

#browser = Browser('firefox')
    url_nasa_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_nasa_jpl)
    html = browser.html
    jpl_soup = BeautifulSoup(html,'html.parser')
    image_jpl = jpl_soup.body.find('img', class_='fancybox-image')
#image


# In[10]:

    featured_image= 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19952_ip.jpg'

    #Append the featured image to the mission to Mars Dictionary.

    mission_to_mars['Featured Image'] = featured_image

# In[11]:

#Scrape the NASA Twitter feed.

    """twitter_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(twitter_url)
    tweet_soup = BeautifulSoup(response.text,'html.parser')
    mars_tweet = tweet_soup.body.find('p')
    #Append the latest Mars Tweet.
    mission_to_mars['Latest Mars Tweet'] = mars_tweet"""


# In[12]:

#mars_weather = str(results)
#print(mars_weather)


# In[13]:

#Use Pandas to scrape the Mars facts website.

    url_table = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(url_table)
#mars_table


# In[14]:

    mars_table_df = mars_table[0]
    mars_table_df.columns = ['Fact','Data']
#mars_table_df


# In[15]:
    #Convert the Mars Table to HTML.
    mars_table_html = mars_table_df.to_html(header=True, index=False)
    #Append the table to the mission to Mars dictionary.
    mission_to_mars['Mars Facts'] = mars_table_html


# In[16]:

    """url_mh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mh)
    html = browser.html
    mars_soup = BeautifulSoup(html,'html.parser')
    hemisphere = mars_soup.find('div',class_='collapsible results')

    results = hemisphere.find('a')
#print(results)


# In[17]:

    hemisphere_list = []

    for result in results:
        title = result.h3
        link = 'https://astrogeology.usgs.gov' + result['href']
        print(title,link)    
        browser.visit(link)
        time.sleep(5)
        image_html = browser.html
        soup = BeautifulSoup(image_html,'html.parser')
        soup_image = soup.find('div', class_='downloads').find('li').a['href']
        print(soup_image)
        mars_images = {'title':title, 'img_url':soup_image}
        mars_hemispheres= hemisphere_list.append(mars_images)
        #Append to mission the mission to Mars dictionary.
        mission_to_mars['Mars Hemispheres'] = mars_hemispheres"""

        #Return mission to Mars Dictionary.
    return mission_to_mars

#print(hemisphere_list)

#Helper function to build the mission to Mars website.
def missionMars(mission_to_mars):
    website = ""
    for p in website:
        website += " " + p.get_text()
        print(website)
    return website    




