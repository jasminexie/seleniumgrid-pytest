import pytest
from application import Application


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")

def pytest_generate_tests(metafunc):
    metafunc.parametrize(
        'browser_name',
        metafunc.config.getoption('browser').split(';'),
        scope='session'
    )

@pytest.fixture(scope='session')
def app(browser_name):
    return Application(browser_name)

@pytest.fixture(autouse=True, scope='session')
def config(app):
    # setup_stuff
    yield
    # teardown_stuff
    app.driver.quit()
