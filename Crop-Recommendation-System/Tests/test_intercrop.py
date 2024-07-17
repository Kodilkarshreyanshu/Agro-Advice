import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestPairCroppingSystem(unittest.TestCase):
    def setUp(self):
        # Set up the web driver with Service object
        chrome_driver_path = "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get('http://127.0.0.1:8000/pair_crop')  # URL of the first page
    
    def test_pair_cropping_option_selection(self):
        # Wait for option links to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul li a'))
        )

        # Click on the first option link
        option_link = self.driver.find_element(By.XPATH, "//ul/li[1]/a")
        option_link.click()

        # Wait for form elements to be present on the second page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'ph'))
        )

        # Find input fields and submit button
        ph_input = self.driver.find_element(By.ID, 'ph')
        temperature_input = self.driver.find_element(By.ID, 'temperature')
        rainfall_input = self.driver.find_element(By.ID, 'rainfall')
        submit_button = self.driver.find_element(By.CLASS_NAME, 'submit-button')

        # Input values to form fields
        ph_input.send_keys('6.5')
        time.sleep(1)  # Pause for 1 second
        temperature_input.send_keys('30')
        time.sleep(1)  # Pause for 1 second
        rainfall_input.send_keys('150')
        time.sleep(1)  # Pause for 1 second

        # Submit the form
        submit_button.click()
        time.sleep(5)  # Wait for the result page to load

        # Assuming you have some verification/assertion logic here
        # For example, you might want to check if a result is displayed after submission
        result_element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'result'))
        )
        self.assertTrue(result_element.is_displayed(), "Result element is not displayed after form submission")
    
    def tearDown(self):
        # Close the browser window after the test
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
