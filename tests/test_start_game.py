import pytest
import allure

@pytest.mark.usefixtures("game_actions")
class TestGardenscapes:
    
    @allure.feature('Launch Game')
    @allure.story('Launch the game and wait for Play button')
    @allure.step('Check if Play button is present after launching the game')
    def test_launch_game(self, game_actions):
        play_button_id = 'com.playrix.gardenscapes:id/play_button'
        game_actions.wait_for_element(play_button_id)
        assert game_actions.is_element_present(play_button_id), "Play button is not present after launching the game."

    @allure.feature('Click Play Button')
    @allure.story('Click the Play button')
    @allure.step('Click Play button and verify it is no longer present')
    def test_click_play_button(self, game_actions):
        play_button_id = 'com.playrix.gardenscapes:id/play_button'
        game_actions.click_element(play_button_id)
        assert not game_actions.is_element_present(play_button_id), "Play button is still present after clicking it."

    @allure.feature('Game Opened')
    @allure.story('Verify the game opened after clicking Play button')
    @allure.step('Verify game screen is present after clicking Play button')
    def test_game_opened(self, game_actions):
        game_screen_id = 'com.playrix.gardenscapes:id/game_screen'
        assert game_actions.is_element_present(game_screen_id), "Game screen did not open after clicking Play button."

    @allure.feature('Start game End-to-End Test')
    @allure.story('Complete end-to-end test')
    @allure.step('Perform end-to-end test from launching the game to verifying game screen')
    def test_start_game_e2e(self, game_actions):
        play_button_id = 'com.playrix.gardenscapes:id/play_button'
        game_screen_id = 'com.playrix.gardenscapes:id/game_screen'
        
        with allure.step('Launch the game and wait for Play button'):
            game_actions.wait_for_element(play_button_id)
            assert game_actions.is_element_present(play_button_id), "Play button is not present after launching the game."
            allure.attach(game_actions.driver.get_screenshot_as_png(), name="Launch Game", attachment_type=allure.attachment_type.PNG)

        with allure.step('Click Play button'):
            game_actions.click_element(play_button_id)
            allure.attach(game_actions.driver.get_screenshot_as_png(), name="Click Play Button", attachment_type=allure.attachment_type.PNG)

        with allure.step('Verify the game screen is present'):
            assert game_actions.is_element_present(game_screen_id), "Game screen did not open after clicking Play button."
            allure.attach(game_actions.driver.get_screenshot_as_png(), name="Game Screen", attachment_type=allure.attachment_type.PNG)
