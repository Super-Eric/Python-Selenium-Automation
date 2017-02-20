import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
chromedriver="C:\\Users\\c.lapenta\\Documents\\chromedriver_win32\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome(chromedriver)
 
    def test_search_in_python_org(self):
        driver = self.driver
        ## Test Case
        driver.get("http://www.rp-online.de/") #Navigate to URL
        self.assertIn("RP ONLINE", driver.title) #Judge if string 1 in string 2
        # Negative Case
        # self.assertIn("Python", driver.title)
       
        #<input name="q" id="header-search-term" type="text" placeholder="Suchbegriff eingeben">
        elem = driver.find_element_by_name("q") #Locate the search box
       
        elem.send_keys("Wetter") #Input search keyword
        elem.send_keys(Keys.RETURN) # Click Enter button
        assert "No results found." not in driver.page_source
        # Negative Case
        # assert "No results found." in driver.page_source
       
        #<div class="hover">
        elems=driver.find_elements_by_class_name("hover")
        print(elems[0].text)
        #//*[@id="search-result-container"]/section/article[1]/a/header/div[2]
 
    def tearDown(self):
        self.driver.close()       
 
if __name__ == "__main__":
    unittest.main()