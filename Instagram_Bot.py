import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD
TARGET_ACCOUNT = TARGET_ACCOUNT


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.follow_count = 0

    def log_in(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        cookies = self.driver.find_element(by=By.CSS_SELECTOR, value="button[tabindex='0']")
        cookies.click()
        time.sleep(2)
        email = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
        email.send_keys(EMAIL)
        password = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(10)
        save_info = self.driver.find_element(by=By.CSS_SELECTOR, value="div[tabindex='0']")
        save_info.click()
        time.sleep(2)
        notifications = self.driver.find_element(by=By.CSS_SELECTOR, value="._a9_1")
        notifications.click()
        time.sleep(2)

    def find_followers(self):
        search_button = self.driver.find_element(by=By.CSS_SELECTOR, value="svg[aria-label='Search']")
        search_button.click()
        time.sleep(2)
        search_input = self.driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label='Search input']")
        search_input.send_keys(TARGET_ACCOUNT)
        time.sleep(2)
        target_account = self.driver.find_element(by=By.CSS_SELECTOR, value=f"a[href='/{TARGET_ACCOUNT}/']")
        target_account.click()
        time.sleep(2)

    def follow(self):
        followers = self.driver.find_element(by=By.CSS_SELECTOR, value=f"a[href='/{TARGET_ACCOUNT}/followers/']")
        followers.click()
        time.sleep(30)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="div.x1uvtmcs div div div div div div div div div div div div div div div div button")
        for button in follow_buttons:
            if self.follow_count > 150:
                break
            try:
                button.click()
                time.sleep(2)
                self.follow_count += 1
            except ElementClickInterceptedException:
                close_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                close_button.click()