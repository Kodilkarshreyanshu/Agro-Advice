import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestFertilizerRecommendationSystem(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get('http://127.0.0.1:8000')

    def test_navigation_to_different_pages(self):
    # Navigate to Crop Prediction page
        self.driver.get('http://127.0.0.1:8000/predi%20ctor')
        time.sleep(1)  # Pause for 1 secondw
        self.assertEqual(self.driver.title, 'Crop Recommendation System')

    # Navigate back to Home page
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(1)  # Pause for 1 second
        self.assertEqual(self.driver.title, 'Home Page CRS')

        # Navigate to Fertilizer Recommendation page
        self.driver.get('http://127.0.0.1:8000/fert_recommend')
        time.sleep(1)  # Pause for 1 second
        self.assertEqual(self.driver.title, 'Fertilizer Recommendation System')

        # Navigate back to Home page
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(1)  # Pause for 1 second
        self.assertEqual(self.driver.title, 'Home Page CRS')

        # Continue similar navigation for other pages...


if __name__ == '__main__':
    unittest.main()
