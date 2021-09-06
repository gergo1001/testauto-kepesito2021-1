import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)

random_color_name_id = "randomColorName"
random_color_id = "randomColor"

test_color_name_id = "testColorName"
test_color_id = "testColor"
start_id = "start"
stop_id = "stop"
result_id = "result"


def get_text_color(id):
    return driver.find_element_by_id(id).text


# visszaadja a szint-t
def getcolor(id):
    return driver.find_element_by_id(id).get_attribute("style")


# ha nincs stilus, akkor nincs szin
def van_szin(s):
    return not s == ""


def test_TC01():
    assert van_szin(getcolor(test_color_id)) is False
    assert get_text_color(test_color_name_id) == ""
    assert van_szin(getcolor(random_color_id)) is True
    assert get_text_color(random_color_name_id) != ""


def jouzenet(sz1, sz2, uzenet):
    if sz1 != sz2:
        if uzenet == "Incorrect!":
            return True
        else:
            return False
    else:
        if uzenet == "Correct!":
            return True
        else:
            return False


# megnézi, hogy startra változnak e a szinek, és leállítja.
def test_TC02():
    kezdoszin = get_text_color(test_color_name_id)
    driver.find_element_by_id(start_id).click()
    time.sleep(5)
    ujszin = get_text_color(test_color_name_id)
    # volt e változás
    print(kezdoszin)
    print(ujszin)
    assert ujszin != kezdoszin
    driver.find_element_by_id(stop_id).click()


# hasonló mint a teszt2 csak, a végén az üzenet helyességét nézi
def test_TC03():
    kezdoszin = get_text_color(test_color_name_id)
    driver.find_element_by_id(start_id).click()
    time.sleep(3)
    ujszin = get_text_color(test_color_name_id)
    # volt e változás
    assert ujszin != kezdoszin
    driver.find_element_by_id(stop_id).click()
    vegsoszin = get_text_color(test_color_name_id)
    baloldaliszin = get_text_color(random_color_name_id)
    assert jouzenet(vegsoszin, baloldaliszin, driver.find_element_by_id(result_id).text) is True
