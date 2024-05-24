from appium import webdriver
from api.game_api import GameAPI

class GameActions:
    def __init__(self, driver: webdriver.Remote, api: GameAPI):
        self.driver = driver
        self.api = api

    def click_by_coordinates(self, x, y):
        self.driver.tap([(x, y)])
        self.api.send_command('click_by_coordinates', {'x': x, 'y': y})

    def click_button(self, button_id):
        coordinates = self.api.get_button_coordinates(button_id)
        self.click_by_coordinates(coordinates['x'], coordinates['y'])
        self.api.click_element(button_id)

    def open_window(self, window_id):
        self.api.open_window(window_id)

    def pass_level(self, start_level, end_level):
        self.api.pass_level(start_level, end_level)

    def wait_for_element(self, element_id, timeout=30):
        return self.driver.find_element_by_id(element_id)

    def click_element(self, element_id):
        element = self.wait_for_element(element_id)
        element.click()
        self.api.click_element(element_id)

    def is_element_present(self, element_id):
        try:
            self.driver.find_element_by_id(element_id)
            return True
        except:
            return False
