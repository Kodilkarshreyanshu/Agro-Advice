import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestCropRecommendationSystem(unittest.TestCase):

    def setUp(self):
        # Set up the web driver with Service object
        chrome_driver_path = "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get('http://127.0.0.1:8000/predi%20ctor') 

    
        

    def test_crop_recommendation_form_submission(self):
        # Wait for form elements to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'N'))
        )

        # Find form elements
        nitrogen_input = self.driver.find_element(By.ID, 'N')
        phosphorus_input = self.driver.find_element(By.ID, 'P')
        potassium_input = self.driver.find_element(By.ID, 'K')
        ph_input = self.driver.find_element(By.ID, 'ph')
        rainfall_input = self.driver.find_element(By.ID, 'R')

        # Use find_element for dropdowns (assuming these are not dynamically populated)
        state_dropdown = Select(self.driver.find_element(By.ID, 'sts'))
        city_dropdown = Select(self.driver.find_element(By.ID, 'state'))

        submit_button = self.driver.find_element(By.ID, 'S')

        # Input values to form fields
        nitrogen_input.send_keys('56')
        time.sleep(1)  # Pause for 1 second
        phosphorus_input.send_keys('65')
        time.sleep(1)  # Pause for 1 second
        potassium_input.send_keys('73')
        time.sleep(1)  # Pause for 1 second
        ph_input.send_keys('6')
        time.sleep(1)  # Pause for 1 second
        rainfall_input.send_keys('189')
        time.sleep(1)  # Pause for 1 second

        # Select state and city (assuming they are populated dynamically)
        state_dropdown.select_by_visible_text('Delhi')
        time.sleep(1)  # Pause for 1 second
        city_dropdown.select_by_visible_text('New Delhi')
        time.sleep(1)  # Pause for 1 second

        # Submit the form
        submit_button.click()
        time.sleep(5)

        # Assuming you have some verification/assertion logic here
        # For example, you might want to check if a result is displayed after submission
        result_element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'crop-result'))
        )
        self.assertTrue(result_element.is_displayed(), "Result element is not displayed after form submission")

if __name__ == '__main__':
    unittest.main()
