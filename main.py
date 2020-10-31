from selenium import webdriver

import time

custom_url = "https://maplestory.nexon.net/News/"

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    brower.get(custom_url)

    news_container = []

    maple_news = brower.find_element_by_class_name("news-wrapper")
    news_ul = maple_news.find_elements_by_tag_name("ul")

    for query_item in news_ul:
        # text_form = query_item.text
        # print (text_form)

        query_innerHTML = query_item.get_attribute("innerHTML")
        query_split_lines = query_innerHTML.strip().splitlines()

        for items in query_split_lines:
            if "href=" in items:
                print (items)



finally:
    try:
        brower.close()
    except:
        pass
