from selenium import webdriver as wd
import chromedriver_binary
import random
import time

# Wait for a random amount of time so that the bot doesn't get flagged.
def PickRandomTime():
    delay = random.randrange(2,10)
    time.sleep(delay)

# Start Chrome and go to the webadrress
wd = wd.Chrome()
wd.implicitly_wait(10)

#Link to the page which contains the item I want to buy.
wd.get("https://www.canadacomputers.com/index.php?cPath=43")

# Function to continue to wait until the item is in stock.
def waitForInstock():
    # Close the popup windows
    close_button = wd.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button/h3')
    PickRandomTime()
    close_button.click()
    PickRandomTime()

    # Get the element that displays if the item is in stock.
    inStock = wd.find_element_by_xpath('/html/body/main/div/section/div[2]/div[2]/div/div/div[2]/div/div/a/div[1]')

    # If the element is not in stock, wait for the item to be in stock.
    while inStock.get_attribute('innerText') != ' Online - Available to Ship':
        PickRandomTime()
        wd.refresh()
    # If the item is found to be in stock, call the buy now function.
    buyNow()

def buyNow():
    # Add the item to the cart.
    addToCart = wd.find_element_by_xpath('/html/body/main/div/section/div[2]/div[2]/div/div/div[2]/div/div/div[2]/a/button')
    PickRandomTime()
    addToCart.click()

    # Click the checkout button.
    secure_checkout = wd.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[1]/button[3]')
    PickRandomTime()
    secure_checkout.click()

    # Enter email information
    PickRandomTime()
    email = wd.find_element_by_id("cm-xp-email")
    email.send_keys("random124@gmail.com")

    # Enter first name.
    PickRandomTime()
    first_name = wd.find_element_by_id("cm-xp-firstname")
    first_name.send_keys("John")

    # Enter last name
    PickRandomTime()
    last_name = wd.find_element_by_id("cm-xp-lastname")
    last_name.send_keys("Doe")

    # Enter Phone number: Area Code - first 3 digits - last 4 digits
    PickRandomTime()
    area_code = wd.find_element_by_id("cm-xp-mobile-areacode")
    area_code.send_keys("416")

    PickRandomTime()
    first_digits = wd.find_element_by_id("cm-xp-mobile-phonenumber-three")
    first_digits.send_keys("555")

    PickRandomTime()
    last_digits = wd.find_element_by_id("cm-xp-mobile-phonenumber-four")
    last_digits.send_keys("5555")

    # Enter Checkout
    PickRandomTime()
    checkout_button = wd.find_element_by_id('cm-btn-checkout')
    checkout_button.click()

#TODO: Finish the rest of the checkout process.
if __name__ == '__main__':
    waitForInstock()