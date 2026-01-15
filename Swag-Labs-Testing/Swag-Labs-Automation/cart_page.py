from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cart_contents_container")))

def get_cart_products(driver):
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_products_names = []
    for item in cart_items:
        cart_products_names.append(item.text)


    print("\n Products in cart:")
    for product in cart_products_names:
        print(f" - {product}")

        return cart_products_names

