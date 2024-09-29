"""Agreement page locators"""


def agree_btn(driver):
    return driver.find_element_by_id("hko.MyObservatory_v1_0:id/btn_agree")


def google_allow_btn(driver):
    return driver.find_element_by_xpath(" //*[@text='Allow'] ")


def background_access_btn(driver):
    return driver.find_element_by_xpath(" //*[@text='OK'] ")


def allow_location_btn(driver):
    return driver.find_element_by_xpath(" //*[@text='Don’t allow'] ")
