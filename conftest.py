import  pytest
import  os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers=['chrome','ch','firefox','ff','headlesschrome']

    browser=os.environ.get('BROWSER',None)
   # driver=webdriver.Chrome()

    if not browser:
        raise Exception("The Environment variable 'BROWSER' must be set")

    browser=browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported")

    if browser in ('chrome','ch'):
        driver = webdriver.Chrome(options=chrome_options)
      #  driver=webdriver.Chrome()
    elif browser in ('firefo','ff'):
        driver=webdriver.Firefox()



    request.cls.driver=driver
   # yield
    #driver.quit()