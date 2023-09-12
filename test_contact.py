import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver_setup import driver_setup

link = 'https://thedemosite.co.uk/'



class Home_page(unittest.TestCase):

    def setUp(self) -> None:
        self.driver_setup = driver_setup()
        self.driver_setup.get(link)

    def test_contact_us(self):
        contact_us_button = WebDriverWait(self.driver_setup, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Contact')]")))
        contact_us_button.click()

        buttons = {
                '//*[@id="post-24"]/div/div/form/div[1]/input':'shalev',
                '//*[@id="post-24"]/div/div/form/div[2]/input':'mor',
                '//*[@id="post-24"]/div/div/form/div[3]/input':'shalev@lama.com',
                '//*[@id="post-24"]/div/div/form/div[4]/textarea':'bugi bugi'

        }
        for xpath, value in buttons.items():
            input_field = WebDriverWait(self.driver_setup, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            input_field.send_keys(value)

        submit_button = WebDriverWait(self.driver_setup, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="post-24"]/div/div/form/div[7]/button')))
        submit_button.click()

        current_url = self.driver_setup.current_url
        assert current_url == 'https://thedemosite.co.uk/contact/'


        success_message_element = WebDriverWait(self.driver_setup, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'The form has been submitted successfully!')]")))
        if success_message_element.is_displayed():
            print("The message appears on the page 'The form has been submitted successfully!' ")
        else:
            print("The message does not appear on the page")
    
    def test_new_button(self):
        a_button = WebDriverWait(self.driver_setup, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="menu-item-22"]/a/span[2]')))
        a_button.click()
    
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver_setup.quit()
