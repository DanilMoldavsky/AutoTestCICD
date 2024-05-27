import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Открывает браузер для каждого теста отдельно, автоматически
@pytest.fixture(scope='function', autouse=True)
def driver(request):
    try:
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        # добавляем драйвер внутрь тестов
        request.cls.driver = driver
        # возвращаем драйвер
        yield driver
    finally:
        driver.quit()