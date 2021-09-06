from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
input_id = "title"
message_xpath = "/html/body/form/span"


# mező kitöltése
def send_input(value):
    driver.find_element_by_id(input_id).clear()
    driver.find_element_by_id(input_id).send_keys(value)


# üzenet lekérdezése
def get_error_value():
    return driver.find_element_by_xpath(message_xpath).text


# helyes értékkel tesztelés
def test_TC01():
    send_input("abcd1234")
    assert "" == get_error_value()


# hibás karakterrel tesztelés, itt elírás van, az üzenet végén nincs pont
def test_TC02():
    send_input("teszt233@")
    assert "Only a-z and 0-9 characters allewed" == get_error_value()


# röviddel tesztelés
def test_TC03():
    send_input("abcd")
    assert "Title should be at least 8 characters; you entered 4." == get_error_value()
    driver.close()
