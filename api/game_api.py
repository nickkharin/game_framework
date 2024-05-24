import requests

class GameAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_command(self, command, params=None, method='POST'):
        url = f"{self.base_url}/{command}"
        if method.upper() == 'PUT':
            response = requests.put(url, json=params)
        else:
            response = requests.post(url, json=params)
        return response.json()

    def get_button_coordinates(self, button_id):
        return self.send_command('get_button_coordinates', {'button_id': button_id})

    def pass_level(self, start_level, end_level):
        return self.send_command('pass_level', {'start_level': start_level, 'end_level': end_level})

    def click_element(self, element_id):
        return self.send_command('click_element', {'element_id': element_id})

    def open_window(self, window_id):
        return self.send_command('open_window', {'window_id': window_id})
        
