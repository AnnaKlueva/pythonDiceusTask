from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.open_positions_page import OpenPositionsPage


class CareersPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    LOCATION_BLOCK = (By.ID, "career-our-location")
    TEAMS_BLOCK = (By.XPATH, '*//h3[contains(text(), "Find your calling")]')
    LIFE_IN_INSIDER_BLOCK = (By.XPATH, '*//h2[contains(text(),"Life at Insider")]')
    QA_JOBS_BUTTON = (By.XPATH, '*//a[contains(text(),"QA jobs")]')

    def is_locations_area_visible(self):
        return self.scroll_to_and_wait_for_visible(self.LOCATION_BLOCK)

    def is_teams_area_visible(self):
        return self.scroll_to_and_wait_for_visible(self.TEAMS_BLOCK)

    def is_life_in_insider_area_visible(self):
        return self.scroll_to_and_wait_for_visible(self.LIFE_IN_INSIDER_BLOCK)

    def click_all_qa_jobs(self):
        self.get_web_element(*self.QA_JOBS_BUTTON).click()
        return OpenPositionsPage(self.driver, self.wait)


