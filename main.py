
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
KEYWORD="buy domain"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
print(search_bar)

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

shitty_element = WebDriverWait(browser,10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "AuVD"))
)

browser.execute_script(
    """
    console.log(arguments);
    const shitty = arguments[0];
    console.log(shitty);
    shitty.parentElement.removeChild(shitty)
    """,
    shitty_element,
)






#search_results = browser.find_element_by_id("rso").find_elements_by_class_name("g")
search_results = browser.find_elements_by_class_name("g")
print(search_results)

#shitty_element = browser.find_element_by_class_name('g jNVrwc Y4pkMc')
for index, search_result in enumerate (search_results):
    #search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
browser.quit()
