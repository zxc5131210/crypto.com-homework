"""hamburger menu page"""


def hamburger_menu_option_forcast(driver):
    return driver.find_elements_by_id("hko.MyObservatory_v1_0:id/expand_image")[0]


def hamburger_menu_option_nine_days(driver):
    return driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='hko.MyObservatory_v1_0:id/title' and @text='9-Day Forecast']"
    )
