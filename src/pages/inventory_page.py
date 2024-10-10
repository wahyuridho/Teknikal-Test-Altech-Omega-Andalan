from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import user_data as ud

class InventoryPage(BasePage):

    # Locators
    productHeader = (By.XPATH, '//span[@class="title"]')
    chartIcon = (By.XPATH, '//a[@class="shopping_cart_link"]')
    chartBadge = (By.XPATH, '//span[@class="shopping_cart_badge"]')

    def getHeaderText(self):
        header = self.find_element(*self.productHeader)
        return header.text
    
    def isHeaderDisplayed(self):
        return self.find_element(*self.productHeader).is_displayed()
    
    def getAddProduct(self, product_name):
        addProduct = (By.XPATH, f'//*[text()="{product_name}"]/parent::*/parent::*/parent::*/child::div[@class="pricebar"]/child::button')
        return addProduct
    
    def addProduct(self, product_name):
        addProduct = self.getAddProduct(product_name)
        self.find_element(*addProduct).click()
    
    def getBtnTxtProduct(self, product_name):
        addProduct = self.getAddProduct(product_name)
        return self.find_element(*addProduct).text
    
    def chartCount(self):
        count = self.find_element(*self.chartBadge)
        return count.text
    
    def moveToCart(self):
        self.find_element(*self.chartIcon).click()