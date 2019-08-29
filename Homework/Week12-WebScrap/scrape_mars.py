from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo

def init_browser():
   
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    scrape_results = {}
    ###NASA MARS NEWS
    url ="https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    latest_title=[]
    latest_paragraphs=[]
    quotes = soup.find_all('li', class_='slide')

    for quote in quotes:
       
        title = quote.find('div',class_="content_title").text
        paragraph = quote.find('div', class_='article_teaser_body').text
        latest_title.append(title)
        latest_paragraphs.append(paragraph)
    
    news_title =  latest_title[0]
    news_p  = latest_paragraphs[0]

    ###JPL MARS SPACE IMAGES
    url_img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_img)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_main = soup.find('article', class_="carousel_item")
    image_a= image_main.find('a',class_="button fancybox")['data-fancybox-href']
    title_main = image_main.find('a',class_="button fancybox")['data-title']
    image_descrip= image_main.find('a',class_="button fancybox")['data-description']
    featured_image_url = ('https://www.jpl.nasa.gov' + image_a)
    featured_image_title = title_main
    featured_image_descrip = image_descrip
    import shutil
    response = requests.get(featured_image_url, stream=True)
    with open('featured_image_url.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    ###MARS WEATHER
    url_tweet = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_tweet)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet_txts=[]
    tweet_imgs = []
    
    tweets = soup.find_all('li', class_='js-stream-item stream-item stream-item')

    # Iterate through each book
    for tweet in tweets:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        tweet_txt_1 = tweet.find('div', class_='js-tweet-text-container').text
        tweet_img = tweet.find('img')['src']
        tweet_img_url = (tweet_img )
        tweet_txt_1 = tweet_txt_1.split('apic')[0]
        tweet_txts.append(tweet_txt_1)
        tweet_imgs.append(tweet_img_url)

    mars_weather = tweet_txts[0]
    mars_weather_img = tweet_imgs[0]
    response = requests.get(mars_weather_img, stream=True)
    with open('mars_weather_img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    ##################   Mars Facts
    import pandas as pd
    url_table = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_table)
    df = tables[0]
    df.columns = ['Characteristic', 'Mars', 'Earth']
    df=df.set_index('Characteristic')
    html_table_mars = df.to_html()
    html_table_mars = html_table_mars.replace('\n', '')
    df_2 = tables[1]
    df_2.columns = ['Characteristic', 'Mars']
    df_2=df_2.set_index('Characteristic')
    html_table_mars_des = df_2.to_html()
    html_table_mars_des = html_table_mars_des.replace('\n', '')
    ### MARS HEMISPHERES
    url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_cerberus)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_image_urls_1={} 
    
    title_cerberus = soup.find('h2', class_='title').text
    img_url_cerberus = soup.find('img',class_='wide-image')['src']
    img_url_cerberus = ('https://astrogeology.usgs.gov' + img_url_cerberus)
    hemisphere_image_urls_1.update({"title":title_cerberus, "img_url":img_url_cerberus })
    response = requests.get(img_url_cerberus, stream=True)
    with open('img_url_cerberus.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_schiaparelli)
    hemisphere_image_urls_2={} 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    title_schiaparelli= soup.find('h2', class_='title').text
    img_url_schiaparelli = soup.find('img',class_='wide-image')['src']
    img_url_schiaparelli = ('https://astrogeology.usgs.gov' + img_url_schiaparelli)
    hemisphere_image_urls_2.update({"title":title_schiaparelli, "img_url":img_url_schiaparelli})
    response = requests.get(img_url_schiaparelli, stream=True)
    with open('img_url_schiaparelli.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    url_syrtis = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url_syrtis)
    hemisphere_image_urls_3={} 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    title_syrtis= soup.find('h2', class_='title').text
    img_url_syrtis = soup.find('img',class_='wide-image')['src']
    img_url_syrtis = ('https://astrogeology.usgs.gov' + img_url_syrtis)
    response = requests.get(img_url_syrtis, stream=True)
    with open('img_url_syrtis.png' ,'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    hemisphere_image_urls_3.update({"title":title_syrtis, "img_url":img_url_syrtis})

    url_Valles = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url_Valles)
    hemisphere_image_urls_4={} 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    title_Valles= soup.find('h2', class_='title').text
    img_url_Valles = soup.find('img',class_='wide-image')['src']
    img_url_Valles = ('https://astrogeology.usgs.gov' + img_url_Valles)
    hemisphere_image_urls_4.update({"title":title_Valles, "img_url":img_url_Valles})
    response = requests.get(img_url_Valles, stream=True)
    with open('img_url_Valles.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    hemisphere_image_urls =[]
    hemisphere_image_urls.append(hemisphere_image_urls_1)
    hemisphere_image_urls.append(hemisphere_image_urls_2)
    hemisphere_image_urls.append(hemisphere_image_urls_3)
    hemisphere_image_urls.append(hemisphere_image_urls_4)

    scrape_results = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url": featured_image_url,
        "featured_image_title" : featured_image_title,
        "featured_image_descrip" : featured_image_descrip,
        "mars_weather" : mars_weather,
        "mars_weather_img" :mars_weather_img,
        "html_table_mars": html_table_mars,
        "html_table_mars_des": html_table_mars_des,
        "hemisphere_image_urls" : hemisphere_image_urls,
        "img_url_cerberus": img_url_cerberus,
        "title_cerberus": title_cerberus,
        "title_schiaparelli": title_schiaparelli,
        "img_url_schiaparelli":img_url_schiaparelli,
        "title_syrtis": title_syrtis,
        "img_url_syrtis":img_url_syrtis,
        "title_Valles": title_Valles,
        "img_url_Valles" : img_url_Valles

    }

    return scrape_results


