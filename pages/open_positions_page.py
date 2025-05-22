import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.jobs_lever_co_page import JobsLeverCoPage


class OpenPositionsPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    DROPDOWN_LOCATION = (By.ID, 'filter-by-location')
    DROPDOWN_DEPARTMENT = (By.ID, 'filter-by-department')
    LIST_POSITIONS = (By.CLASS_NAME, 'position-title')
    LIST_LOCATIONS = (By.CLASS_NAME, 'position-location')
    LIST_DEPARTMENTS = (By.CLASS_NAME, 'position-department')
    LIST_OF_JOBS = (By.CSS_SELECTOR, '.position-list-item-wrapper a')

    @allure.step("Select value {location_name} in dropbox location")
    def select_by_location(self, location_name):
        self.wait_util_header_is_loaded()
        dropdown_location_web_element = self.get_web_element(*self.DROPDOWN_LOCATION)
        dropdown = Select(dropdown_location_web_element)
        dropdown.select_by_visible_text(location_name)

    @allure.step("Select value {department_name} in dropbox department")
    def select_by_department(self, department_name):
        dropdown_department_web_element = self.get_web_element(*self.DROPDOWN_DEPARTMENT)
        dropdown = Select(dropdown_department_web_element)
        dropdown.select_by_visible_text(department_name)

    def list_jobs_contains_position(self, position):
        self.scroll_to_and_wait_for_visible(self.LIST_POSITIONS)
        list_of_elems = self.driver.find_elements(*self.LIST_POSITIONS)
        return  all(position in el.text.strip() for el in list_of_elems)

    def list_jobs_contains_location(self, location):
        list_of_elems = self.driver.find_elements(*self.LIST_LOCATIONS)
        return all(location in el.text.strip() for el in list_of_elems)

    def list_jobs_contains_department(self, department):
        list_of_elems = self.driver.find_elements(*self.LIST_DEPARTMENTS)
        return all(department in el.text.strip() for el in list_of_elems)

    def select_first_job_opportunity(self):
        first_elem = 0
        first_elem = self.driver.find_elements(*self.LIST_OF_JOBS)[first_elem]
        first_elem.click()
        self.switch_to_new_tab()
        return JobsLeverCoPage(self.driver, self.wait)
