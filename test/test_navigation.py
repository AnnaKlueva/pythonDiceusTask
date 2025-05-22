import allure

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from test.base_test import BaseTest


@allure.title("Insider navigation test")
class TestInsider(BaseTest):

    def test_home_page_is_loading(self):
        expected_url = "https://useinsider.com/"
        home_page = HomePage(self.driver, self.wait)
        home_page.go_to_home_page()
        home_page.wait_util_header_is_loaded()
        assert expected_url == home_page.get_url()

    def test_navigation_to_careers_page(self):
        home_page = HomePage(self.driver, self.wait)
        home_page.go_to_home_page()
        home_page.wait_util_header_is_loaded()
        home_page.navigate_to_company_tab()
        careers_page = home_page.navigate_to_careers_page()

        # Verify the Careers page is opened.
        url = careers_page.get_url()
        assert "careers" in url, "Careers page is not open"

        # Ensure the presence of the following sections:
        assert careers_page.is_locations_area_visible(), "Locations area is not visible"
        assert careers_page.is_teams_area_visible(), "Teams area is not visible"
        assert careers_page.is_life_in_insider_area_visible(), "Life in Insider area is not visible"

    def test_filter_by_qa(self):
        QA_CAREERS_URL = "https://useinsider.com/careers/quality-assurance/"
        location = "Istanbul, Turkiye"
        department = "Quality Assurance"
        position = "Quality Assurance"

        careers_page = CareersPage(self.driver, self.wait)
        careers_page.go_to_page(QA_CAREERS_URL)
        careers_page.close_cookies_window()
        open_position_page = careers_page.click_all_qa_jobs()

        open_position_page.select_by_location(location)
        open_position_page.select_by_department(department)

        assert open_position_page.list_jobs_contains_position(position)
        assert open_position_page.list_jobs_contains_location(location)
        assert open_position_page.list_jobs_contains_department(department)

        # Click on the “View Role” button for any job.
        jobs_lever_co_page = open_position_page.select_first_job_opportunity()

        #Verify that the user is redirected to a Lever.co application form page.
        assert position in jobs_lever_co_page.get_job_title()





