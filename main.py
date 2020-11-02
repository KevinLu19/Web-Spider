from selenium import webdriver

import time
import validators

# custom_url = "https://maplestory.nexon.net/News/"

def grab_URL(query_data):
    new_string = query_data.split('href="')[1].split('"')[0]

    return new_string

def validify_URL(checking_url):
    valid_url = validators.url(checking_url)

    if valid_url == True:
        return checking_url

if __name__ == "__main__":
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        brower = webdriver.Firefox(firefox_options=fireFoxOptions)

        user_input_url = input ("Enter URL: ")
        working_url = validify_URL(user_input_url)

        brower.get(str(working_url))
        maple_news = brower.find_element_by_class_name("news-wrapper")
        news_ul = maple_news.find_elements_by_tag_name("ul")

        query_container = []

        for query_item in news_ul:
            query_innerHTML = query_item.get_attribute("innerHTML")
            query_split_lines = query_innerHTML.strip().split()

            for items in query_split_lines:
                if "href=" in items:
                    each_items = grab_URL(items)
                    query_container.append(each_items)

    finally:
        try:
            brower.close()
        except:
            pass
