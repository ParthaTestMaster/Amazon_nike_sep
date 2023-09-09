import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utils import Utils



##head less run
options = Options()
options.headless = False
url = "https://www.amazon.co.uk/Nike-Park-Short-Sport-Shorts/dp/B07W5XYSSJ/ref=sr_1_10?crid=32RIA2KO1I72J&keywords=nike&qid=1686722397&sprefix=nike%2Caps%2C113&sr=8-10&th=1&psc=1"
##inialize webdriver
#driver = webdriver.Edge(options=options)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
## driver.get() to get in to mentioned urll
driver.get(
    "https://www.amazon.co.uk/Nike-Park-Short-Sport-Shorts/dp/B07W5XYSSJ/ref=sr_1_10?crid=32RIA2KO1I72J&keywords=nike&qid=1686722397&sprefix=nike%2Caps%2C113&sr=8-10&th=1&psc=1")
driver.maximize_window()
## accept cookies
accept_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='sp-cc-accept']")))
accept_cookies_button.click()
## new search item
driver.find_element(By.CSS_SELECTOR, "input[id='twotabsearchtextbox']").clear()
driver.find_element(By.CSS_SELECTOR, "input[id='twotabsearchtextbox']").send_keys("adidas")
driver.find_element(By.CSS_SELECTOR,"input[id='nav-search-submit-button']").click()
time.sleep(3)
## get search details from search page
ele = driver.find_element(By.CSS_SELECTOR,"div[class='a-section a-spacing-small a-spacing-top-small']").text
ele_2=ele.replace('1-48 of', '')
print(ele_2)
driver.close()

# ##get product title
# product_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='productTitle']")))
# print("product name :", product_title.text)
#
# ##select size large
# drop_down = driver.find_element(By.CSS_SELECTOR, 'select[name="dropdown_selected_size_name"]')
# select = Select(drop_down)
# select.select_by_visible_text("XL")
# size = 'L'
# print("product size :", size)
# time.sleep(3)
# ##get product value
# product_value = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")))
# print("Price of the item : ", product_value.text + 'cents')
#
# ## click on add to basket
# driver.refresh()
# add_to_basket = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[id='submit.add-to-cart']")))
# add_to_basket.click()
#
# ## Basket page
# element = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]')))
# print('Status :', element.text)
# time.sleep(3)
# basket_subtotal  = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='a-price sw-subtotal-amount']")))
# print('basket sun total : ', basket_subtotal.text)

