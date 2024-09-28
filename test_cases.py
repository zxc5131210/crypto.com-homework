import utils
from gesture import Gesture


class TestCases:

    def __init__(self):
        utils.delete_file("nine_days_page.png")
        self.driver = utils.connect_driver()
        self.gesture = Gesture(self.driver)

    def task_1(self):
        self.gesture.skip_agreement_page()
        self.gesture.skip_main_page_ads()
        self.gesture.redirect_to_nine_days_page()
        for i in range(2):
            self.gesture.scroll_down_the_page()
        self.gesture.screenshot_if_nine_days_later()


if __name__ == "__main__":
    TestCases().task_1()
