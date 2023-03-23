# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from time import sleep

# Set up Chrome options to disable images
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)


# Launching the browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Navigating to the URL
driver.get("https://www.automationexercise.com")

# Verifying that home page is visible successfully
assert "Automation Exercise" in driver.title

# Clicking on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# Verifying 'New User Signup!' is visible
assert "New User Signup!" in driver.page_source

# Entering name and email address
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)").send_keys("testuser@example.com")

# Clicking 'Signup' button
driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button").click()

# Verifying 'ENTER ACCOUNT INFORMATION' is visible
assert "Enter Account Information" in driver.page_source

# Filling details
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "password").send_keys("test123")
driver.find_element(By.NAME, "days").send_keys("26")
driver.find_element(By.NAME, "months").send_keys("March")
driver.find_element(By.NAME, "years").send_keys("1988")

# Selecting checkbox 'Sign up for our newsletter!'
driver.execute_script("window.scrollTo(0,400)")
driver.find_element(By.CSS_SELECTOR, "#newsletter").click()

# Selecting checkbox 'Receive special offers from our partners!'
driver.find_element(By.CSS_SELECTOR, "#optin").click()

# Filling details
driver.find_element(By.NAME, "first_name").send_keys("User")
driver.find_element(By.NAME, "last_name").send_keys("Test")
driver.find_element(By.NAME, "company").send_keys("Test Company")
driver.find_element(By.NAME, "address1").send_keys("123 Test Address")
driver.find_element(By.NAME, "address2").send_keys("Apt 101")
driver.find_element(By.NAME, "country").send_keys("United States")
driver.find_element(By.NAME, "state").send_keys("New York")
driver.find_element(By.NAME, "city").send_keys("New York City")
driver.find_element(By.NAME, "zipcode").send_keys("10001")
driver.find_element(By.NAME, "mobile_number").send_keys("1234567890")

# Clicking 'Create Account' button
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()

# Verifying 'ACCOUNT CREATED!' is visible
assert "Account Created!" in driver.page_source

# Clicking 'Continue' button
driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()

# Verifying 'Logged in as username' is visible
assert "Logged in as" in driver.page_source

# Clicking 'Delete Account' button
driver.find_element(By.LINK_TEXT, "Delete Account").click()
