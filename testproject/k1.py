from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
input_a_id = "a"
input_b_id = "b"
result_id = "result"
results_visible_id = "results"
submit_id = "submit"


def fill_inputmezo(input_id, value):
    driver.find_element_by_id(input_id).clear()
    driver.find_element_by_id(input_id).send_keys(value)


def get_inputmezo(input_id):
    return driver.find_element_by_id(input_id).text


def get_result_text(result_id):
    return driver.find_element_by_id(result_id).text


# láthatóságot vizsgálná
def get_result_text_visible(result_id):
    s = driver.find_element_by_id(results_visible_id).get_attribute("style")
    if s == "display: inline;":
        return True
    else:
        return False


# lekéri az induló állapotot és azt ellenőrzi
def test_TC01():
    assert get_inputmezo(input_a_id) == ""
    assert get_inputmezo(input_b_id) == ""
    assert get_result_text(result_id) == ""
    assert get_result_text_visible(results_visible_id) is False


# valós értékekkel tesztel
def test_TC02():
    fill_inputmezo(input_a_id, "2")
    fill_inputmezo(input_b_id, "3")
    driver.find_element_by_id(submit_id).click()
    assert get_result_text(result_id) == "10"
    assert get_result_text_visible(results_visible_id) is True


# üress mezőkkel tesztel
def test_TC03():
    fill_inputmezo(input_a_id, "")
    fill_inputmezo(input_b_id, "")
    driver.find_element_by_id(submit_id).click()
    assert get_result_text(result_id) == "NaN"
    assert get_result_text_visible(results_visible_id) is True
    driver.close()

