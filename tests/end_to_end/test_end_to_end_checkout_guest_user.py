
import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.CheckoutPage import CheckOutPage
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
import time

@pytest.mark.usefixtures('init_driver')
class TestEndtoEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        # Creating page objects
        home_p=HomePage(self.driver)
        header=Header(self.driver)
        cart_p=CartPage(self.driver)
        checkout_p=CheckOutPage(self.driver)
        orderReceived_p=OrderReceivedPage(self.driver)

        # go to home page

        home_p.go_to_home_page()

        # add 1 item to the cart

        home_p.click_first_add_to_cart_btn()

        # make sure number is updated before adding to cart

        #time.sleep(3)
        header.wait_until_cart_item_count(1)
        # go to cart
        header.click_on_cart_on_right_header()

        product_names=cart_p.get_all_product_names_in_cart()

        assert len(product_names)==1,f"Expected 1 item in cart but found {len(product_names)}"

        # apply free coupon

        COUPON_CODE=GenericConfigs.FREE_COUPONS

        cart_p.apply_coupon(COUPON_CODE)

        # select free shipping

        # click on proceed to checkout

        cart_p.click_on_proceed_to_checkout()

        # fill in the form

        checkout_p.fill_in_billing_info()

        # click on place order

        checkout_p.click_place_order()

        # verify order is received

        orderReceived_p.verify_order_received_page_loaded()

        # verify order is recorded in DB (via SQL or via API)



