
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
print(search_bar)

search_bar.send_keys("hello")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_element_by_id("rso").find_elements_by_class_name("g")
print(search_results)

for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3");

    if(title):
        print("***********")
        print(title.text)
