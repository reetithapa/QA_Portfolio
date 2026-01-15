from driver_setup import setup_driver
from login_page import login
from inventory_page import list_product, open_each_product_and_add_to_cart, remove_all_products_from_inventory
from cart_page import go_to_cart, get_cart_products
from selenium.webdriver.common.by import By
import time

def test_saucedemo_end_to_end():
    driver = setup_driver()

    try:
        login(driver)

        list_product(driver)

        added_products = open_each_product_and_add_to_cart(driver)

        go_to_cart(driver)

        cart_products = get_cart_products(driver)

        assert set(added_products) == set(cart_products)
        print("\n Cart Verification Successful")

        driver.find_element(By.ID, "continue-shopping").click()
        remove_all_products_from_inventory(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    test_saucedemo_end_to_end()


