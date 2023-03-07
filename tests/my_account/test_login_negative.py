import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        my_Account=MyAccountSignedOut(self.driver)

        #goto my account

        my_Account.go_to_my_account()
        #type username
        my_Account.input_login_username('Nikita')
        # type password

        my_Account.input_login_password('Hello123')
         #click login
        my_Account.click_on_login()
        #verify errormessge

        Expected_err="Error: The username Nikita is not registered on this site. If you are unsure of your username, try your email address instead."

        my_Account.wait_until_error_is_displayed(Expected_err)



