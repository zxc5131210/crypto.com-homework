"""main_page locators"""


def exit_btn(driver):
    return driver.find_element_by_id("hko.MyObservatory_v1_0:id/exit_btn")


def hamburger_menu_btn(driver):
    return driver.find_element_by_xpath(
        "//android.widget.ImageButton[@content-desc='Navigate up']"
    )
