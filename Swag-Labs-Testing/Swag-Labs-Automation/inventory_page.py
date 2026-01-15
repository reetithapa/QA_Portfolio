from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def list_product(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name ")
    print(f"Total Products: {len(products)}")

    for i, product in enumerate(products, 1):
        print(f"{i}. {product.text}")

    return products

def open_each_product_and_add_to_cart(driver):
    added_products = []

    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    total_products = len(products)

    for index in range(total_products):
        products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_name = products[index].text
        print(f"\nOpening: {product_name}")

        products[index].click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_container")))

        driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
        print(f"Added to cart: {product_name}")
        added_products.append(product_name)

        driver.find_element(By.ID, "back-to-products").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_container")))

    return added_products

def remove_all_products_from_inventory(driver):
    remove_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_secondary")

    for button in remove_buttons:
        button.click()

        print("All products removed from inventory")




