from selenium import webdriver

import time

custom_url = "https://maplestory.nexon.net/News/"

def grab_URL(query_data):
    new_string = query_data.split('href="')[1].split('"')[0]

    return new_string

if __name__ == "__main__":
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        brower = webdriver.Firefox(firefox_options=fireFoxOptions)

        brower.get(custom_url)
        maple_news = brower.find_element_by_class_name("news-wrapper")
        news_ul = maple_news.find_elements_by_tag_name("ul")

        for query_item in news_ul:
        # text_form = query_item.text
        # print (text_form)

            query_innerHTML = query_item.get_attribute("innerHTML")
            query_split_lines = query_innerHTML.strip().split()

            #print (query_split_lines)

            for items in query_split_lines:
                if "href=" in items:
                    #query_href = items.split()
                    # query_container.append(items)

                    print(grab_URL(items))

    finally:
        try:
            brower.close()
        except:
            pass

    query_container = []
