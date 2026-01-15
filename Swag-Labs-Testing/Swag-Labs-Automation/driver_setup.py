from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    print(driver.title)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    assert "inventory.html" in driver.current_url, "Login didnot redirect to inventory page"
    print("Login successful")

    return driver

def list_products(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print(f"Total products: {len(products)}")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product.text}")
    return products

def open_products_and_add_to_cart(driver, products_element):
    product_name = products_element.text
    products_element.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name")))

    driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    print(f"Added {product_name} to cart")
    return product_name

def test_login_and_inventory():
    driver = setup_driver()
    try:
        login(driver)

        products = list_products(driver)

        selected_product_name = open_products_and_add_to_cart(driver, products[0])

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Browser closed")


if __name__ == "__main__":
    test_login_and_inventory()



