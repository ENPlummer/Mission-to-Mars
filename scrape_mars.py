
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
    mission_to_mars['Headline'] = title
    #news_title = str(results_title)
    #print(news_title)

    paragraph = soup.find('div', class_='rollover_description_inner').text

    #Append Mars news headline to the dictionary.
    mission_to_mars["Article"] = paragraph
    #news_p = str(result_p)
    #print(news_p)


    # Use Splinter to scrape the NASA JPL page.

    browser = Browser('firefox')
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)
    html = browser.html
    soup_div = BeautifulSoup(html,'html.parser')
    featured_image = soup_div.find('img', class_='thumb')




    #featured_image= 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19952_ip.jpg'

    #Append the featured image to the mission to Mars Dictionary.
    mission_to_mars['Featured_Image'] = featured_image


    #Scrape the Mars weather Twitter feed.
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(tweet_url)
    soup_tweet = BeautifulSoup(response.text,'html.parser')
    recent_tweet = soup_tweet('p',class_='TweetTextSize')[0]
    
    #Append the tweet to the mission_to_mars dictionary.
    mission_to_mars['Weather_tweet'] = recent_tweet





    #Use Pandas to scrape the Mars facts website.

    url_table = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(url_table)
    #mars_table




    mars_table_df = mars_table[0]
    mars_table_df.columns = ['Fact','Data']
    #mars_table_df


    #Convert the Mars Table to HTML.
    mars_table_html = mars_table_df.to_html(header=True, index=False)
    #Append the table to the mission to Mars dictionary.
    mars_table_dict = []
    mars_table_dict.append(mars_table_html)
    mission_to_mars['Mars Facts'] = mars_table_dict


    #url_mh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #browser.visit(url_mh)
    #html = browser.html
    #mars_soup = BeautifulSoup(html,'html.parser')
    #hemisphere = mars_soup.find('div',class_='collapsible results')

    #results = hemisphere.find('a')


    #hemisphere_list = []

    #for result in results:
        #title = result.h3
        #link = 'https://astrogeology.usgs.gov' + result['href']
        #print(title,link)    
        #browser.visit(link)
        #time.sleep(5)
        #image_html = browser.html
        #soup = BeautifulSoup(image_html,'html.parser')
        #soup_image = soup.find('div', class_='downloads').find('li').a['href']
        #print(soup_image)
        #mars_images = {'title':title, 'img_url':soup_image}
        #mars_hemispheres= hemisphere_list.append(mars_images)
        #Append to mission the mission to Mars dictionary.
        #mission_to_mars['Mars Hemispheres'] = mars_hemispheres