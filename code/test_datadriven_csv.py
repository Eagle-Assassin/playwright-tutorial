from playwright.sync_api import Page,expect
import pytest
import csv

#Read the Json File
logindata=[]
with open("testdata/data.csv",newline="",encoding="utf-8") as r:
    reader=csv.DictReader(r)
    for row in reader:
        logindata.append((row['email'],row['password'],row['validity']))


@pytest.mark.parametrize("email,password,validity",logindata)
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