from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import platform


### DEFINE PARAMETERS

if platform.platform().strip().split('-')[0] == "Linux":
    # Path to ChromeDriver
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver' # Insert your chromedrive path (which chromedriver)
    BROWSER_PATH = '/usr/bin/chromium-browser' # Insert your chromium path (which chromium-browser)

    # Set up the Chrome WebDriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = BROWSER_PATH

elif platform.platform().strip().split('-')[0] == "macOS":
    CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver' # Insert your chromium path
    
    # Set up the Chrome WebDriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver with the specified path
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Define the router details
ROUTER_IP = "192.168.1.1" # Change to your router IP address
USERNAME = "admin" # Change to your router username
PASSWORD = "admin" # Change to your router password


### MAIN BODY

# Open the router login page
print("Opening router login page...")
driver.get(f"http://{ROUTER_IP}")

# Wait for the username field to be present in the DOM
print("Waiting for username field...")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pc-login-user")))

# Find the username field element by its id attribute
username_field = driver.find_element(By.ID, "pc-login-user")
username_field.send_keys(USERNAME)
print("Username entered.")

# Find the password field element by its id attribute
print("Waiting for password field...")
password_field = driver.find_element(By.ID, "pc-login-password")
password_field.send_keys(PASSWORD)
print("Password entered.")

# Submit the login form
print("Submitting login form...")
login_field = driver.find_element(By.ID, "pc-login-btn")
login_field.click()

# Wait for possible popup and handle it
try:
    print("Checking for force login popup...")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "confirm-yes")))
    force_login_button = driver.find_element(By.ID, "confirm-yes")
    force_login_button.click()
    print("Force login confirmed.")
except:
    print("No force login popup detected.")

# Wait for the next page to load
print("Waiting for login to complete...")
time.sleep(5)  # Adjust based on your router's response time

# Check if login was successful by looking for a specific element on the landing page
try:
    print("Checking login status...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "advanced")))
    print("Login successful.")
except:
    print("Login failed.")
    driver.quit()
    exit()

# Navigate to the Access Control page
print("Navigating to Access Control page...")

# Click on the "Advanced" button
advanced_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "advanced")))
advanced_button.click()
print("Advanced menu clicked.")

# Click on the "Security" icon
security_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "security")))
security_icon.click()
print("Security icon clicked.")

# Wait for the "Access Control" link to be clickable and then click it
access_control_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@url='accessControl.htm']")))
access_control_link.click()
print("Access Control link clicked.")

# Verify that we are on the Access Control page by checking the class attribute
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@url='accessControl.htm' and contains(@class, 'sel clicked')]")))
    print("Navigated to Access Control page successfully.")
except:
    print("Failed to navigate to Access Control page.")
    driver.quit()
    exit()

# Check the current state and toggle it using JavaScript
print("Checking current Access Control state...")
time.sleep(5)  # Wait for the page to fully load
acl_on_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ACLOn")))
acl_off_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ACLOff")))

print(f"Initial ACL On button class: {acl_on_button.get_attribute('class')}")
print(f"Initial ACL Off button class: {acl_off_button.get_attribute('class')}")

if "selected" in acl_on_button.get_attribute("class"):
    print("Access Control is currently enabled. Disabling it.")
    driver.execute_script("arguments[0].click();", acl_off_button)  # Disable Access Control
    time.sleep(5)  # Wait for the action to take effect
    print(f"Post-click ACL On button class: {acl_on_button.get_attribute('class')}")
    print(f"Post-click ACL Off button class: {acl_off_button.get_attribute('class')}")
else:
    print("Access Control is currently disabled. Enabling and then disabling it.")
    driver.execute_script("arguments[0].click();", acl_on_button)  # Enable Access Control
    time.sleep(5)
    print(f"Post-enable ACL On button class: {acl_on_button.get_attribute('class')}")
    print(f"Post-enable ACL Off button class: {acl_off_button.get_attribute('class')}")
    driver.execute_script("arguments[0].click();", acl_off_button)  # Disable Access Control
    time.sleep(5)  # Wait for the action to take effect
    print(f"Final-click ACL On button class: {acl_on_button.get_attribute('class')}")
    print(f"Final-click ACL Off button class: {acl_off_button.get_attribute('class')}")

# Log out
print("Logging out...")
logout_button = driver.find_element(By.ID, "topLogout")
logout_button.click()
print("Logout button clicked.")

# Wait for the logout confirmation popup and click the "Yes" button
try:
    print("Waiting for logout confirmation popup...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='button-button green pure-button btn-msg btn-msg-ok btn-confirm']")))
    confirm_logout_button = driver.find_element(By.XPATH, "//button[@class='button-button green pure-button btn-msg btn-msg-ok btn-confirm']")
    confirm_logout_button.click()
    print("Confirmed logout.")
except:
    print("No logout confirmation popup detected.")

# Close the browser
print("Closing browser...")
driver.quit()
print("Script completed.")
