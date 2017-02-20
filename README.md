# Python Selenium Automation for Windows

## 1. Installation
### 1) Python
* Link: https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe
  * Download and run the installation wizard, please remember to tick "*Add Python 3.6 to Path*" option.
  * Then click "Install Now", follow the installation wizard to install Python.

### 2) Pip
* This is a good tool of Python for installing Python packages. We will use this to get selenium package. It has been installed in first step of Python installation.

### 3) Selenium
* Link: http://selenium-python.readthedocs.io/installation.html
  * Run the following command to install selenium:
  >**python -m pip install selenium**  
  >**python -m pip --proxy proxy.server:port install selenium** #behind proxy

### 4) Liclipse
* Link: http://www.liclipse.com/download.html
  * Follow the installation wizard and install Liclipse.
  * It is a good IDE to be used to program our test cases and run them.

### 5) Webdriver
* Chrome driver:
  * Link: https://sites.google.com/a/chromium.org/chromedriver/downloads
  * The latest version is 2.27
* Firefox:
  * It would be recommended to install Firefox on Laptop, then use selenium with it. There is no need of other downloaded driver.

## 2. Tutorial
### 1) Start Liclipse and create New Project
* Click on “File”
  * NEW >>> PyDev Project
  * Add a new Project name (Example “TEST”)
  * Grammar version 3.6
  * Interpreter “Default”
  * Click on “Finish”
* Create new file:
  * Right click on the Project name (“TEST”)
  * Go to “NEW” >>> “File”, create a new file. (like “Test.py”)
  * Click on “Finish”
  * You created a new file and now you can add the script below to this file.
  * Please be aware, that you have to update the “Chromedriver” part in the script.
* Start The script:
  * Now you can start the script:
  * Right click on the project name
  * Click on “Run as”
  * Click on “1 Run Python”
* Sample Code: [sample.py](https://github.com/Super-Eric/Python-Selenium-Automation/blob/master/sample.py)
* Use Case 01: [uc01.py](https://github.com/Super-Eric/Python-Selenium-Automation/blob/master/uc01.py)
