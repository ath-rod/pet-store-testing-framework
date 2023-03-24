from driver import ChromeDriver


class UIBaseClassTest:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = ChromeDriver()
        cls.driver = cls.driver.driver

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
