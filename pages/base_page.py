import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC


class BasePage(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Open URL: {url}")
    def go_to_page(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    @allure.step("Close cookies window...")
    def close_cookies_window(self):
        close_cookies_tab = self.get_web_element(By.XPATH, "*//a[contains(text(),'Decline All')]")
        close_cookies_tab.click()

    def is_element_present(self, locator):
        try:
            self.driver.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def wait_until_clickable(self, element, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d:
                                         element.is_displayed() and element.is_enabled())

    def wait_util_header_is_loaded(self):
        element = self.driver.find_element(By.XPATH, '*//a[contains(text(),"Get a Demo")]/parent::li')
        time_to_sleep = int(element.get_attribute("data-animate-delay"))
        time.sleep(time_to_sleep)

    def scroll_to_and_wait_for_visible(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except Exception as e:
            print(f"Error scrolling to element {locator}: {e}")
            return False

    def get_multiple(self, *locator):
        return self.browser.find_elements(*locator)

    def click(self, *by_locator):
        self.get(*by_locator).click()

    @allure.step("Switch to new tab...")
    def switch_to_new_tab(self):
        current_handles = self.driver.window_handles
        self.driver.switch_to.window(current_handles[-1])
