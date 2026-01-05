from playwright.sync_api import Page,expect
from loginpage import LoginPage
from homepage import HomePage
from cartpage import CartPage
import pytest

@pytest.mark.parametrize("username,password,product_name",[("pavanol","test@123","Samsung galaxy s6")])
def test_user_can_login_and_add_product_to_cart(page:Page,username,password,product_name):
    page.goto("https://www.demoblaze.com/")

    #Login
    login=LoginPage(page)

    login.click_login_link()
    login.enter_username(username)
    login.enter_password(password)
    login.login_button()

    #homepage
    homepage=HomePage(page)

    homepage.add_product_to_cart(product_name)
    homepage.gotocart()

    #cartpage
    cartpage=CartPage(page)

    product=cartpage.check_product_in_cart(product_name)
    print(product.text_content())
    page.wait_for_timeout(5000)
    expect(product).to_have_count(1)

