from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youtube.com/results?search_query=" + "sachin+tendulkar")

results = driver.find_elements_by_xpath('//div[@class="yt-lockup-content"]')

print(len(results))

for result in results:
    video = result.find_element_by_xpath('.//h3/a')
    title = video.get_attribute('title')
    url = video.get_attribute('href')
    print("{} ({})".format(title, url).encode('UTF-8'))
driver.quit()