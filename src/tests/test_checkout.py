import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CekoutPage
from data import user_data as ud

class TestCheckoutScenario:
    @pytest.mark.checkOut
    def test_checkout_product(self, browser: WebDriver):
        login = LoginPage(browser)
        home = InventoryPage(browser)
        cart = CartPage(browser)
        cekout = CekoutPage(browser)
        login.open()
        login.inputCredential('standard_user','secret_sauce')
        login.submit()
        browser.implicitly_wait(10)

        # Cek apakah halaman sudah pindah ke home page
        assert browser.current_url == ud.inventory_url, "Url tidak sesuai"
        assert home.isHeaderDisplayed, "Header Product tidak muncul"
        assert home.getHeaderText() == 'Products', "Header Text yang tidak sesuai"

        # Add product
        products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
        prices = ["$29.99", "$9.99", "$15.99"]
        for i in range(len(products)):
            home.addProduct(products[i])

        # Cek button add to chart berubah menjadi remove
        for i in range(len(products)):
            assert home.getBtnTxtProduct(products[i]) == 'Remove', 'Button tidak berubah'

        assert int(home.chartCount()) == len(products), 'Jumlah barang tidak sesuai'

        # Pindah ke halaman checkout
        home.moveToCart()
        browser.implicitly_wait(10)

        # cek apakah halaman sudah pindah ke cart page
        assert browser.current_url == ud.cart_url, 'Url tidak sesuai'
        assert cart.isHeaderDisplayed(), 'Header tidak muncul'
        assert cart.getHeaderText() == 'Your Cart', 'Header Text tidak sesuai'

        # Cek barang yang sudah di add to chart
        listProduct = cart.getListProduct()
        listProductPrice = cart.getListProductPrice()
        for i, (actual_product, actual_price, expected_product, expected_price) in enumerate(zip(listProduct, listProductPrice, products, prices)):
            assert actual_product == expected_product, f'Expected Product name {expected_product}, Actual Product name {actual_product}'
            assert actual_price == expected_price, f'Expected Product Price {expected_price}, Actual Product price {actual_price}'

        # cekout barang
        cart.checkout()
        browser.implicitly_wait(10)
        assert browser.current_url == ud.cekout_one_url, 'Url tidak sesuai'
        assert cekout.isHeaderDisplayed(), 'Header tidak muncul'
        assert cekout.getHeaderText() == 'Checkout: Your Information', 'Header Text tidak sesuai'

        # isi form
        cekout.fillform('Zero', 'Bantai', 911)
        
        # menuju halaman selanjutnya
        cekout.submit()
        browser.implicitly_wait(10)
        assert browser.current_url == ud.cekout_two_url, 'Url tidak sesuai'
        assert cekout.isHeaderDisplayed(), 'Header tidak muncul'
        assert cekout.getHeaderText() == 'Checkout: Overview', 'Header Text tidak sesuai'

        overviewProduct = cekout.getListProduct()
        overviewPrice = cekout.getListProductPrice()

        for i, (act_prod, act_price, ex_prod, ex_price) in enumerate(zip(overviewProduct, overviewPrice, products, prices)):
            assert act_prod == ex_prod, f'Expected Result {ex_prod}, Actual Result {act_prod}'
            assert act_price == ex_price, f'Expected Result {ex_price}, Actual Result {act_price}'
        
        subtotal = cekout.getSubtotal()
        tax = cekout.getTax()
        total = cekout.getTotalPrice()
        subtotalPrice = cekout.countTotal(prices)
        taxPrice = cekout.countTax(subtotalPrice)
        totalPrice = cekout.sumPrice(subtotalPrice, taxPrice)

        assert float(subtotal[13:]) == subtotalPrice, 'Subtotal tidak sama'
        assert float(tax[6:]) == taxPrice, 'Tax tidak sama'
        assert float(total[8:]) == totalPrice, 'Total tidak sama'

        cekout.submitFinish()
        browser.implicitly_wait(10)
        assert browser.current_url == ud.complete_url, 'Url tidak sesuai'
        assert cekout.isHeaderDisplayed(), 'Header tidak muncul'
        assert cekout.getHeaderText() == 'Checkout: Complete!', 'Header Text tidak sesuai'

        assert cekout.iconSuccesVisible(), 'Icon tidak muncul'
        assert cekout.getCompleteHeaderText() == 'Thank you for your order!', 'Text tidak sesuai'
        assert cekout.getCompleteText() == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!', 'Text tidak sesuai'


        time.sleep(1)
        