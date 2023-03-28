# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and already registered email address
# 7. Click 'Signup' button
# 8. Verify error 'Email Address already exist!' is visible

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

# Click on the 'Signup / Login' button
signup_login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Signup / Login']"))
)
signup_login_button.click()

# Verify that 'New User Signup' is visible
assert 'New User Signup!' in driver.page_source

# Enter name and already registered email address
name_input = driver.find_element(By.NAME, "name")
email_input = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)")
signup_button = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button")

name_input.send_keys('Test User')
email_input.send_keys('testuser@example.com')
signup_button.click()

# Verify error message is visible
error_message = driver.find_element(By.XPATH, "//p[normalize-space()='Email Address already exist!']")
assert 'Email Address already exist!' in error_message.text

# Quit browser
driver.quit()
