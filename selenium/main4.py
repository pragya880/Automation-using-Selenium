from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the Chrome driver
s = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("NAME OF THE WEBSITE")

# Use WebDriverWait to wait for the element to be interactable
wait = WebDriverWait(driver, 10)

# Define a function to retry the action until success or timeout
def retry_action(action, max_attempts=5, delay=2):
    for _ in range(max_attempts):
        try:
            return action()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying...")
            time.sleep(delay)
    raise Exception("Failed after multiple attempts.")

# Find and interact with the EmployeeID field
retry_action(lambda: wait.until(EC.element_to_be_clickable((By.NAME, "EmployeeID")))).send_keys("ID")

# Find and click the send OTP button
retry_action(lambda: wait.until(EC.element_to_be_clickable((By.ID, "send-otp")))).click()

# Assuming there might be a delay in the OTP field becoming available
retry_action(lambda: wait.until(EC.element_to_be_clickable((By.NAME, "otp")))).send_keys("PASSWORD")

# Find and click the verify OTP button
retry_action(lambda: wait.until(EC.element_to_be_clickable((By.ID, "send-otp-verify")))).click()

# Wait for the page title to match the expected title indicating a successful login
retry_action(lambda: wait.until(EC.title_is("HOPEPAGE")))

# After successful login, navigate to the new URL
driver.get("https://HYPERLINK")

# Re-locate the "Add" button after the page transition
retry_action(lambda: wait.until(EC.element_to_be_clickable((By.ID, "add-lead-sidebar-btn")))).click()

# Save a screenshot to a specific path (Ensure the directory exists or adjust the path accordingly)
driver.save_screenshot("NAME.png")

# Consider adding error handling or more checks here as needed

# Example: Close the driver after operations or when an error occurs
# driver.close()
