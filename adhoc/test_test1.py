class TestSuit:
    def test_1(self, app):
        app.driver.get('http://console.appadhoc.com')
        assert 'A/B Testing' in app.driver.title

    def test_2(self, app):
        app.driver.get('http://www.bing.com')
        assert True
