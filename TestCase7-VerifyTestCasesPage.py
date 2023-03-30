# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to url 'http://automationexercise.com'
driver.get('http://automationexercise.com')

# Verify that home page is visible successfully
assert 'Automation Exercise' in driver.title

#Click on 'Test Cases' button
test_cases_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Test Cases']")
test_cases_btn.click()

