# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Launch the browser and navigate to the url
driver = webdriver.Chrome()
driver.get("http://automationexercise.com")

# Verify that the home page is visible
assert "Automation Exercise" in driver.title

# Click on the 'Signup / Login' button
signup_login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Signup / Login']"))
)
signup_login_button.click()

# Verify that 'Login to your account' is visible
assert "Login to your account" in driver.page_source

# Enter correct email address and password
email_input = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
email_input.send_keys("testuser@example.com")
password_input.send_keys("test123")

# Click the 'login' button
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_button.click()

# Verify that 'Logged in as username' is visible
assert "Logged in as" in driver.page_source

# Click the 'Delete Account' button
delete_account_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Delete Account']"))
)
delete_account_button.click()

sleep(5)

# Close the browser
driver.quit()
