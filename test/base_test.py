import builtins
import warnings
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if builtins.driver_name == 'chrome':
            self.driver = webdriver.Chrome()
        elif builtins.driver_name == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()