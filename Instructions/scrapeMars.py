#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Automates browser actions
from splinter import Browser
# Parses the html
from bs4 import BeautifulSoup as bs
import requests
import time
import os

executable_path = {"executable_path": "C:/Users/csuch/OneDrive/Desktop/UNC-CHA-DATA-PT-09-2019-U-C/12-Web-Scraping-and-Document-Databases/2/Activities/08-Stu_Splinter/Solved/Chromedriver/chromedriver.exe"}
browser=Browser("chrome", **executable_path, headless=False)

# Set an empty dict for listings that we can save to Mongo
listings = {}
  
    # URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    # Call visit on our browser and pass in the url we want to scrape
browser.visit(url)

    # Return all of the html on our page
html = browser.html
    #return html


# In[2]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(html, 'html5lib')


# In[3]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[4]:


# Identify and return title of listing
news_title = soup.find('div', class_="content_title").text
news_title


# In[5]:


news_p = soup.find('div', class_="article_teaser_body").text
news_p


# In[6]:


featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23515_hires.jpg'


# In[7]:


# URL of page to be scraped
twitter_url = 'https://twitter.com/marswxreport?lang=en'
# Call visit on our browser and pass in the url we want to scrape
browser.visit(twitter_url)

# Return all of the html on our page
twitter_html = browser.html
#return html
# Create BeautifulSoup object; parse with 'html.parser'
twitter_soup = bs(twitter_html, 'html5lib')
# Examine the results, then determine element that contains sought info

print(twitter_soup.prettify())


# In[8]:


# Identify and return climate on Mars from twitter
Mars_weather = twitter_soup.find('div', class_="js-tweet-text-container").text
print(f'The climate in Mars is:', Mars_weather)


# In[9]:


# URL of page to be scraped
facts_url = 'https://space-facts.com/mars/'
# Call visit on our browser and pass in the url we want to scrape
browser.visit(facts_url)

# Return all of the html on our page
facts_html = browser.html
#return html
# Create BeautifulSoup object; parse with 'html.parser'
facts_soup = bs(facts_html, 'html5lib')
# Examine the results, then determine element that contains sought info

print(facts_soup.prettify())


# In[10]:


# Visit the Mars Facts Site Using Pandas to Read
mars_facts_df = pd.read_html("https://space-facts.com/mars/")[0]
mars_facts_df.columns=["Description", "Value"]
mars_facts_df.set_index("Description", inplace=True)
mars_facts_df


# In[11]:


# URL of page to be scraped
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
# Call visit on our browser and pass in the url we want to scrape
browser.visit(hemisphere_url)

# Return all of the html on our page
hemisphere_html = browser.html
#return html
# Create BeautifulSoup object; parse with 'html.parser'
hemisphere_soup = bs(hemisphere_html, 'html5lib')
# Examine the results, then determine element that contains sought info

print(hemisphere_soup.prettify())


# In[12]:


# Populate a list with links for the hemispheres
hemi_strings = []
links = hemisphere_soup.find_all('h3')

for hemi in links:
    hemi_strings.append(hemi.text)
    
hemi_strings


# In[13]:


executable_path = {"executable_path": "C:/Users/csuch/OneDrive/Desktop/UNC-CHA-DATA-PT-09-2019-U-C/12-Web-Scraping-and-Document-Databases/2/Activities/08-Stu_Splinter/Solved/Chromedriver/chromedriver.exe"}
browser=Browser("chrome", **executable_path, headless=False)
hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere_url)

# Navigating to hemisphere image site
hemisphere_html = browser.html
hemisphere_soup = bs(hemisphere_html, 'html5lib')


# In[14]:


cerberus = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
schiaparelli = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
syrtis_major = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
valles_marineris = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'


# In[18]:


img_links = [cerberus, schiaparelli, syrtis_major, valles_marineris]
a = hemisphere_soup.find_all('h3')
descriptions = [h3.text.strip() for h3 in a]

hemisphere_image_url = [{'title': descriptions, 'img_url': img_links} for descrtiption,link in zip(descriptions, img_links)]
hemisphere_image_url


# In[ ]:




