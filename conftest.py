import pytest
from appium import webdriver
from api.game_api import GameAPI
from actions.game_actions import GameActions
from config.config import BASE_URL, APP_PACKAGE, APP_ACTIVITY, PLATFORM_NAME, DEVICE_NAME

@pytest.fixture(scope='module')
def driver():
    desired_caps = {
        'platformName': PLATFORM_NAME,
        'deviceName': DEVICE_NAME,
        'appPackage': APP_PACKAGE,
        'appActivity': APP_ACTIVITY
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

@pytest.fixture(scope='module')
def game_api():
    return GameAPI(BASE_URL)

@pytest.fixture(scope='module')
def game_actions(driver, game_api):
    return GameActions(driver, game_api)
