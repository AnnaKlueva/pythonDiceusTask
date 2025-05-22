import builtins
import warnings
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        is_ci = os.getenv("CI") == "true"
        warnings.simplefilter("ignore", ResourceWarning)

        if builtins.driver_name == 'chrome':
            options = ChromeOptions()
            if is_ci:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument(f"--user-data-dir=/tmp/chrome-user-data-{os.getpid()}")
            self.driver = webdriver.Chrome(options=options)

        elif builtins.driver_name == 'firefox':
            options = FirefoxOptions()
            if is_ci:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)

        else:
            raise Exception("Incorrect Browser")

        if not is_ci:
            try:
                self.driver.maximize_window()
            except Exception:
                pass

        self.wait = WebDriverWait(self.driver, 10)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()