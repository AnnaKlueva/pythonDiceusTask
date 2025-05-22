import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class JobsLeverCoPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, 2)

    @allure.step("Get job title")
    def get_job_title(self):
        title = (By.CSS_SELECTOR, '.posting-headline h2')
        return self.get_web_element(*title).text


