from selenium import webdriver

class Application:
    def __init__(self, browser_name, platform):
        self.driver = webdriver.Remote(
            command_executor = 'http://localhost:4444/wd/hub',
            desired_capabilities = {
                'browserName': browser_name,
                'platform': platform
            }
        )
