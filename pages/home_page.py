import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.careers_page import CareersPage

HOME_PAGE_URL = "https://useinsider.com/"

class HomePage(BasePage):
    def __init__(self, driver, wait):
        self.url = HOME_PAGE_URL
        super().__init__(driver, wait)

    LOGO = (By.CSS_SELECTOR, "img[alt='insider_logo']")
    COMPANY_TAB = (By.XPATH, "//*[@id='navbarDropdownMenuLink'][contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "*//a[contains(text(),'Careers')]")


    def go_to_home_page(self):
        super().go_to_page(self.url)

    @allure.step("Is logo displayed")
    def is_logo_present(self):
        return self.is_element_present(self.LOGO)

    @allure.step("Navigate to 'Company' tab")
    def navigate_to_company_tab(self):
        self.get_web_element(*self.COMPANY_TAB).click()

    @allure.step("Navigate to 'Careers' page")
    def navigate_to_careers_page(self):
        self.get_web_element(*self.CAREERS_LINK).click()
        return CareersPage(self.driver,self.wait)
