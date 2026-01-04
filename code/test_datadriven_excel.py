from playwright.sync_api import Page,expect
import pytest
import openpyxl

#Read the excel File
logindata=[]
workbook=openpyxl.load_workbook("testdata/data.xlsx")
sheet=workbook['Sheet1'] #or workbook.active -> for only one sheet

for row in sheet.iter_rows(min_row=2,values_only=True):
    email,pass_,validity=row
    logindata.append((str(email or ""),str(pass_ or ""),str(validity or  "")))

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