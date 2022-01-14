
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenshooter:
    def __init__(self, keyword, screenshots_dir, max_page=4):

        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword=keyword
        self.screenshots_dir = screenshots_dir
        self.max_page = max_page

    def start(self):
        self.browser.get("https://google.com")        
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        print(search_bar)

        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        try:
            shitty_element = WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "AuVD"))
            )

            self.browser.execute_script(
                """
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty)
                """,
                shitty_element,
            )
        except Exception:
            pass


        def screenshot_bot(search_results, page_num):
            for index, search_result in enumerate(search_results):
                search_result.screenshot(f"{self.screenshots_dir}/{page_num}-{self.keyword}x{index}.png")

        def searching_bot():
            search_results = self.browser.find_elements_by_class_name("g")
            current_page = self.browser.find_element_by_class_name("YyVfkd")
            next_page = self.browser.find_element_by_id("pnnext")
            if int(current_page.text) < self.max_page and next_page :
                screenshot_bot(search_results, int(current_page.text))
                next_page.click()
                searching_bot()
            else:
                screenshot_bot(search_results, int(current_page.text))

        searching_bot()
       

    def finish(self):
        self.browser.quit()



domain_competitors = GoogleKeywordScreenshooter("buy domain","screenshots")
domain_competitors.start()
domain_competitors.finish()


python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()
