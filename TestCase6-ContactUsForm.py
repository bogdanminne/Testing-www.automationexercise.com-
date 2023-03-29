# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# 11. Click 'Home' button and verify that landed to home page successfully

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Navigate to url 'http://automationexercise.com'
driver.get('http://automationexercise.com')

# Verify that home page is visible successfully
assert 'Automation Exercise' in driver.title

#Click on 'Contact Us' button
contact_us_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Contact us']")))
contact_us_btn.click()

#Verify 'GET IN TOUCH' is visible
assert 'Get In Touch' in driver.page_source

#Enter name, email, subject and message
name_input = wait.until(EC.visibility_of_element_located((By.NAME, 'name')))
name_input.send_keys('John Doe')
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('johndoe@example.com')
subject_input = driver.find_element(By.NAME, 'subject')
subject_input.send_keys('Test Subject')
message_input = driver.find_element(By.NAME, 'message')
message_input.send_keys('Test Message')

#Upload file

#Click 'Submit' button
driver.execute_script("window.scrollTo(0,400)")
submit_button = driver.find_element(By.XPATH, "//input[@name='submit']")
submit_button.click()

#Click OK button
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

#Verify success message 'Success! Your details have been submitted successfully.' is visible
assert "Success! Your details have been submitted successfully." in driver.page_source

#Click 'Home' button and verify that landed to home page successfully
home_button = driver.find_element(By.XPATH, "//a[@class='btn btn-success']")
home_button.click()


