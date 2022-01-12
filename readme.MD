### 파이썬 셀레니움
#### web driver api

https://selenium-python.readthedocs.io/api.html

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

```
1. DeprecationWarning: executable_path has been deprecated, please pass in a Service object. -> 이 경고 메세지는 아래와 같이 해결.

from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

2. 크롬 창이 없어지는 문제는.. 아래와 같이 해결했어요. 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

셀레니움 버전때문에.. 니코쌤과 차이가 있나봐요. ㅜㅜ3 install selenium==3.141