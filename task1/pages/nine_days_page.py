"""nine days page"""

from task1 import utils


def menu_area(driver):
    return driver.find_elements_by_xpath(
        "//android.widget.ListView[@resource-id='hko.MyObservatory_v1_0:id/mainAppSevenDayView']//android.widget.LinearLayout"
    )


def nine_days_after_date(driver):
    return driver.find_elements_by_xpath(
        "//android.widget.ListView[@resource-id='hko.MyObservatory_v1_0:id/mainAppSevenDayView']//android.widget.LinearLayout//android.widget.TextView"
    )


def find_element_by_nine_days_after_date(driver):
    return driver.find_element_by_xpath(
        f"//*[contains(@text, '{utils.nine_days_later_date()}')]"
    )
