import time

from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException

from pages import agreement_page, main_page, hamburger_page, nine_days_page

import utils
from logger import Logger


class Gesture:

    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError("driver can not be null.")
        self.driver = driver

    def skip_agreement_page(self):
        """skip the agreement page"""
        agreement_page.agree_btn(self.driver).click()
        agreement_page.agree_btn(self.driver).click()
        agreement_page.google_allow_btn(self.driver).click()
        agreement_page.background_access_btn(self.driver).click()
        agreement_page.allow_location_btn(self.driver).click()

    def skip_main_page_ads(self):
        """skip the ads to main page"""
        time.sleep(3)  # wait for the page to load
        main_page.exit_btn(self.driver).click()
        main_page.exit_btn(self.driver).click()
        time.sleep(1)  # wait for the page to load
        main_page.exit_btn(self.driver).click()
        time.sleep(2)  # wait for the page to load

    def redirect_to_nine_days_page(self):
        """redirect to nine days page"""
        main_page.hamburger_menu_btn(self.driver).click()
        time.sleep(1)  # wait for the page to load
        hamburger_page.hamburger_menu_option_forcast(self.driver).click()
        hamburger_page.hamburger_menu_option_nine_days(self.driver).click()

    def scroll_down_the_page(self, start_y=0.85, stop_y=0.20, duration=2000):
        """swipe up the page"""
        x = self.driver.get_window_size()["width"]  # 取得螢幕的寬
        y = self.driver.get_window_size()["height"]
        x1 = int(x * 0.5)
        y1 = int(y * start_y)
        x2 = int(x * 0.5)
        y2 = int(y * stop_y)
        self.driver.swipe(x1, y1, x2, y2, duration)

    def screenshot_if_nine_days_later(self):
        try:
            if nine_days_page.nine_days_after_date(self.driver):
                self.driver.save_screenshot("nine_days_page.png")
        except NoSuchElementException:
            self.logger.error("The nine days page is not available.")
