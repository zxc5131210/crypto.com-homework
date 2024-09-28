import os
import time

from datetime import datetime, timedelta
from venv import logger

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import config

app_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "apk/MyObservatory_5.9_APKPure.apk")
)


def connect_driver():
    """
    Connect to the UI Automator2 driver.
    """
    desired_caps = dict()
    desired_caps["platformName"] = config.platformName
    desired_caps["platformVersion"] = config.platformVersion
    desired_caps["deviceName"] = config.deviceName
    desired_caps["appPackage"] = config.app_package
    desired_caps["appActivity"] = config.app_activity
    desired_caps["app"] = app_path

    driver = webdriver.Remote(
        f"http://{config.host}:{config.port}/wd/hub", desired_caps
    )

    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    except Exception as e:
        print(f"Error initializing driver: {e}")

    WebDriverWait(driver, 2)
    driver.implicitly_wait(config.implicitly_wait_timeout)

    return driver


def close_driver(driver):
    """
    Quit the driver.
    """
    driver.quit()


def nine_days_later_date():
    """
    Get the date of nine days later.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=9)
    formatted_date = future_date.strftime("%-d %b")

    return formatted_date


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)  # 删除文件
            logger.info(f"file '{file_path}' delete complete")
        else:
            logger.info(f"file '{file_path}' is not exist")
    except Exception as e:
        logger.error(f"there are some error during deleting the file: {e}")
