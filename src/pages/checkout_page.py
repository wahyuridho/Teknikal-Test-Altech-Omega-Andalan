from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import user_data as ud

class CekoutPage(BasePage):

    # Locators
    cartHeader = (By.XPATH, '//span[@class="title"]')
    firstName = (By.ID, 'first-name')
    lastName = (By.ID, 'last-name')
    zipCode = (By.ID, 'postal-code')
    nextBtn = (By.ID, 'continue')
    cancelBtn = (By.ID, 'cancel')
    finishBtn = (By.ID, 'finish')
    productItem = (By.XPATH, '//div[@class="inventory_item_name"]')
    productItemPrice = (By.XPATH, '//div[@class="inventory_item_price"]')
    subtotalPrice = (By.XPATH, '//div[@class="summary_subtotal_label"]')
    taxPrice = (By.XPATH, '//div[@class="summary_tax_label"]')
    totalPrice = (By.XPATH, '//div[@class="summary_total_label"]')
    iconSucces = (By.XPATH, '//img[@class="pony_express"]')
    completeHeader = (By.XPATH, '//h2[@class="complete-header"]')
    completeText = (By.XPATH, '//div[@class="complete-text"]')
    HomeBtn = (By.XPATH, '//button[@data-test="back-to-products"]')


    def getHeaderText(self):
        header = self.find_element(*self.cartHeader)
        return header.text
    
    def isHeaderDisplayed(self):
        return self.find_element(*self.cartHeader).is_displayed()
    
    def fillform(self, firstName, lastName, zipCode):
        self.find_element(*self.firstName).send_keys(firstName)
        self.find_element(*self.lastName).send_keys(lastName)
        self.find_element(*self.zipCode).send_keys(zipCode)

    def submit(self):
        self.find_element(*self.nextBtn).click()

    def cancel(self):
        self.find_element(*self.cancelBtn).click()

    def submitFinish(self):
        self.find_element(*self.finishBtn).click()

    def getListProduct(self):
        items = self.find_elements(*self.productItem)
        product_names = [item.text for item in items]
        return product_names
    
    def getListProductPrice(self):
        items = self.find_elements(*self.productItemPrice)
        product_prices = [item.text for item in items]
        return product_prices
    
    def getSubtotal(self):
        subtotal = self.find_element(*self.subtotalPrice)
        return subtotal.text
    
    def getTax(self):
        tax = self.find_element(*self.taxPrice)
        return tax.text
    
    def getTotalPrice(self):
        total = self.find_element(*self.totalPrice)
        return total.text
    
    def countTotal(self, prices):
        convert_prices = [float(price.replace('$', '')) for price in prices]
        total = 0
        for i in range(len(prices)):
            total = total + convert_prices[i]

        return total
    
    def countTax(self, subTotal):
        tax = round(subTotal * 8 / 100,2)
        return tax
    
    def sumPrice(self, subTotal, Tax):
        total = subTotal + Tax
        return total
    
    def iconSuccesVisible(self):
        return self.find_element(*self.iconSucces).is_displayed()

    def getCompleteHeaderText(self):
        text = self.find_element(*self.completeHeader)
        return text.text
    
    def getCompleteText(self):
        text = self.find_element(*self.completeText)
        return text.text