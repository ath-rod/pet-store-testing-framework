from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    _instances = {}

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(ChromeDriver, cls).__new__(cls)
        return cls._instances[cls]

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
