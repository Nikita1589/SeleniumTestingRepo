import pytest

from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn

@pytest.mark.usefixtures("init_driver")
class TestRregisterNewUser:

    @pytest.mark.tcid13
    def test_regsiter_valid_new_user(self):

        my_account_o=MyAccountSignedOut(self.driver)
        my_account_i=MyAccountSignedIn(self.driver)

        #go to account

        my_account_o.go_to_my_account()
        # fill in username

        rand_email=generate_random_email_and_password()
        my_account_o.input_register_email(rand_email["email"])
        # fill in password
        my_account_o.input_register_password('HelloWorld123#')
        # register account

        my_account_o.click_register_btn()


        # verify user is registered

        my_account_i.verify_user_is_signed_in()