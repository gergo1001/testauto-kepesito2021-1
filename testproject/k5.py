from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(URL)
bingo_mezo_xpath = '//*[@id="bingo-body"]/tr/td/input'
number_count_xpath = '//*[@id="numbers-list"]/li'
init_id = "init"


def get_bingo_number():
    return driver.find_elements_by_xpath(bingo_mezo_xpath)


def get_number():
    return driver.find_elements_by_xpath(number_count_xpath)


def get_bingonumbers():
    szamok = []
    bingoszamok = get_bingo_number()
    for elem in bingoszamok:
        szamok.append(elem.get_property("value"))
    return szamok


# első különbségnél kilép, hogy jó
def van_kulonbseg(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return True
    return False


# 25 és 75 mező

def test_TC01():
    assert len(get_bingo_number()) == 25
    assert len(get_number()) == 75


# feltölti a számokat a bingo tábla értékeivel, majd megnyomjuk az init gombot, újra lekérjük a táblát és azt összehasonlitjuk
def test_TC03():
    szamok_kezd = get_bingonumbers()
    driver.find_element_by_id(init_id).click()
    szamok_uj = get_bingonumbers()
    assert van_kulonbseg(szamok_kezd, szamok_uj) is True
