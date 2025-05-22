import allure
import pytest
import logging


def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="chrome", help="Browser driver to use. Possible options: chrome, firefox"
    )

@pytest.fixture(autouse=True)
def driver_name(request):
    driver_name = request.config.getoption("--driver")
    logging.info(f"Driver name from CLI: {driver_name}")

    import builtins
    builtins.driver_name = driver_name

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Try to get 'self' instance (your test class)
        test_instance = item.instance

        if hasattr(test_instance, "driver"):
            driver = test_instance.driver
            if driver:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

