from playwright.sync_api import Page, expect
import pytest


search_items=['laptop','Gift Card','smartphone','monitor']

@pytest.mark.skip
@pytest.mark.parametrize("item",search_items)
def test_searchites(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item) #We need to pass the itemname
    page.locator("input[value='Search']").click()


    #Assertion
    firs_result=page.locator("h2 a").nth(0)
    expect(firs_result).to_contain_text(item,ignore_case=True)
    
login_testdata=[("laura.taylor1234@example.com","test123","valid"),
                ("invaliduser@example.com","test321","invalid"),
                ("validuser@example.com","testxyz","invalid"),
                ("","","invalid")
                ]
@pytest.mark.parametrize("email,password,validity",login_testdata)
def test_login_datadriven(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator(".ico-login").click()
    #Fill the form
    # print(email,password)
    page.locator("#Email").fill(email)#Email
    page.locator("input[name='Password']").fill(password)
    page.locator("input[value='Log in']").click()

    #validity
    if validity=="valid":
        logout_link=page.locator(".ico-logout")
        expect(logout_link).to_be_visible(timeout=5000)
        print("test")
    else:
        error=page.locator(".validation-summary-errors")
        expect(error).to_be_visible(timeout=5000)

        expect(page).to_have_url("https://demowebshop.tricentis.com/login")

