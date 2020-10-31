from selenium import webdriver

custom_url = "https://maplestory.nexon.net/News/"

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    brower.get(custom_url)

    news_container = []

    # news = brower.find_element_by_class_name("news-wrapper")
    # print_news = news.get_attribute("innerHTML")
    # print (print_news)

    #news_xpath = brower.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/ul")
    #news_xpath = brower.find_elements_by_xpath("//*[@href]")

    news_xpath = brower.find_element_by_xpath("//*[@class='news-wrapper']")
    print (news_xpath.get_attribute("innerHTML"))

    # for hrefs in news_xpath:
    #     print (hrefs.get_attribute("href"))

finally:
    try:
        brower.close()
    except:
        pass
