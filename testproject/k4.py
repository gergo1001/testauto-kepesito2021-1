import string

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)
muveleti_tabla_xpath = "/html/body/div/div/p[3]"
chr_id = "chr"
op_id = "op"
num_id = "num"
result_id = "result"
button_id = "submit"

ABCstabla = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# lekéri a kiírt értéket
def get_muveletitabla_value():
    time.sleep(2)
    return driver.find_element_by_xpath(muveleti_tabla_xpath).text


def get_value(id):
    return driver.find_element_by_id(id).text


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_goog_op(s):
    return s in ('+', '-')


def click_button():
    driver.find_element_by_id(button_id).click()
    return driver.find_element_by_id(result_id).text


# visszaadja hányadik pozicióban van
def poz_char(char):
    for i in range(len(ABCstabla)):
        if ABCstabla[i] == char:
            return i
    return -1


# indulási tábla kiírás értékét ellenőrzi
def test_TC01():
    assert get_muveletitabla_value() == ABCstabla


def test_TC02():
    chr_value = get_value(chr_id)
    # csk egy karakter legyen
    assert len(chr_value) == 1
    # az ascii karakter
    assert is_ascii(chr_value) is True

    op_value = get_value(op_id)
    # csak plusz vagy minusz
    assert is_goog_op(op_value) is True

    num_value = get_value(num_id)
    # szám-e
    assert num_value.isdigit() is True


def test_TC03():
    chr_value = get_value(chr_id)
    op_value = get_value(op_id)
    num_value = get_value(num_id)
    result_value = click_button()
    if op_value == '+':
        assert ABCstabla[poz_char(chr_value) + int(num_value)] == result_value
    if op_value == '-':
        assert ABCstabla[poz_char(chr_value) - int(num_value)] == result_value
    driver.close()