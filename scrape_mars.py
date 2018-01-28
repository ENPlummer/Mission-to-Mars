
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

mission_to_mars = {}

def scrape():

    browser = init_browser()

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
    mission_to_mars["headline"] = title
    #news_title = str(results_title)
    #print(news_title)

    paragraph = soup.find('div', class_='rollover_description_inner').text

    #Append Mars news headline to the dictionary.
    mission_to_mars["article"] = paragraph
    #news_p = str(result_p)
    #print(news_p)


    #Use Splinter to scrape the NASA JPL page.

    browser = Browser('firefox')
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)
    html = browser.html
    soup_div = BeautifulSoup(html,'html.parser')
    image_results = soup_div.find('img', class_='thumb')
    image_src = image_results['src']
    featured_image = 'https://www.jpl.nasa.gov/' + image_src


    #Append the featured image to the mission to Mars Dictionary.
    mission_to_mars['featured_image'] = featured_image


    #Scrape the Mars weather Twitter feed.
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(tweet_url)
    soup_tweet = BeautifulSoup(response.text,'html.parser')
    recent_tweet = soup_tweet.find('p',class_='TweetTextSize').text
    
    #Append the tweet to the mission_to_mars dictionary.
    mission_to_mars['weather_tweet'] = recent_tweet





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
    mission_to_mars['mars_facts_table'] = mars_table_html


    url_mh = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mh)
    html = browser.html
    mars_soup = BeautifulSoup(html,'html.parser')
    hemisphere = mars_soup.find('div',class_='collapsible results')

    results = hemisphere.find('a')


    hemisphere_list = []

    for result in results:
        if result.h3:
            title = result.h3
            link = 'https://astrogeology.usgs.gov'
            print(title,link)    
            browser.visit(link)
            time.sleep(5)
            image_html = browser.html
            soup_scrape = BeautifulSoup(image_html,'html.parser') + result['href']
            soup_image = soup_scrape.find('div', class_='downloads').find('li').a['href']
            print(soup_image)
            mars_images = {'title':title, 'img_url':soup_image}
            hemisphere_list.append(mars_images)
           #Grab each image link for each hemisphere.
            print(hemisphere_list)
            #Grab each image link and append them all to the mission_to_mars dictionary.
            #Cerberus
            cerberus = hemisphere_list[0]['img_url']
            mission_to_mars['cerberus'] = cerberus_hemisphere
            #Shciaparelli
            schiaparelli = hemisphere_list[1]['img_url']
            mission_to_mars['schiaparelli'] = schiaparelli_hemisphere
            #Syrtis Major
            syrtis_major = hemisphere_list[2]['img_url']
            mission_to_mars['syrtis_major'] = syrtis_major_hemisphere
            #Valles Marineris
            valles_marineris = hemisphere_list[3]['img_url']
            mission_to_mars['valles_marineris'] = valles_marineris_hemisphere


    return mission_to_mars    
      