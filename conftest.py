import pytest
from application import Application


def pytest_addoption(parser):
    parser.addoption("--addconfig", action="append", default=[], help="Add a platform and its supported browsers. Format: platform:browser1,browser2")

def pytest_generate_tests(metafunc):
    platform_browsers = []
    for config in metafunc.config.getoption('addconfig'):
        platform = config.split(':')[0]
        browsers = config.split(':')[1].split(',')
        platform_browsers += map(lambda x: (x, platform), browsers)
    metafunc.parametrize(
        'browser_name, platform',
        platform_browsers,
        scope='session'
    )

@pytest.fixture(scope='session')
def app(browser_name, platform):
    """
    Returns an application that initializes a webdriver instance
    :param browser_name: Name of browser
    :param platform: Name of platform
    :return: Application
    """
    return Application(browser_name, platform)

@pytest.fixture(autouse=True, scope='session')
def config(app):
    """
    Cleanup code that quits the browser after session end
    :param app: Application instance
    """
    yield
    app.driver.quit()