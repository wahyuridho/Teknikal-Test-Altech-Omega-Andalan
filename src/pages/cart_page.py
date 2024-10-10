from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import user_data as ud

class CartPage(BasePage):

    # Locators
    cartHeader = (By.XPATH, '//span[@class="title"]')
    productItem = (By.XPATH, '//div[@class="inventory_item_name"]')
    productItemPrice = (By.XPATH, '//div[@class="inventory_item_price"]')
    checkoutBtn = (By.ID, 'checkout')
    backToShopBTN = (By.ID, 'continue-shopping')

    def getHeaderText(self):
        header = self.find_element(*self.cartHeader)
        return header.text
    
    def isHeaderDisplayed(self):
        return self.find_element(*self.cartHeader).is_displayed()
    
    def getListProduct(self):
        items = self.find_elements(*self.productItem)
        product_names = [item.text for item in items]
        return product_names
    
    def getListProductPrice(self):
        items = self.find_elements(*self.productItemPrice)
        product_prices = [item.text for item in items]
        return product_prices
    
    def backToHome(self):
        self.find_element(*self.backToHome).click()

    def checkout(self):
        self.find_element(*self.checkoutBtn).click()