from playwright.sync_api import Page,expect,Playwright
import pytest

#page-> tab, popup,window
#browser>chromium,firefox,webkit etc


#Browser -> context(user profiles) -> page/s
@pytest.mark.skip
def test_multiplecontext(playwright:Playwright):
    
    browser=playwright.chromium.launch(headless=False)

    context=browser.new_context()

    page1=context.new_page()
    page2=context.new_page()

    page1.goto("https://selenium.dev")
    #do some work on it
    expect(page1).not_to_have_title("Selenium automates browsers. That's it!")
    

    page2.goto("https://playwright.dev")
    expect(page2).not_to_have_title("Playwright enables reliable end-to-end testing for modern web apps.")


@pytest.mark.skip
def test_popups(playwright:Playwright):

    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page= context.new_page()

    page.goto("https://testautomationpractice.blogspot.com")

    page.on("popup",lambda popup:popup.wait_for_load_state())

    page.locator("#PopUp").click()

    page.wait_for_timeout(5000)

    #how many pages are present in the context

    all_popups=context.pages

    print("The total number of pop-ups are {}".format(len(all_popups)))

       #Iterate through all the pop-ups and do somting on the playwright page
    for pw in all_popups:
        print(pw.title(),pw.url)
        if pw.title()=="Fast and reliable end-to-end testing for modern web apps | Playwright":
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(3000)

            expect(pw).to_have_title("Installation | Playwright")

            pw.close()
        
    browser.close()

#Direct Approach, Inject userlogin with URL
@pytest.mark.skip
def test_autheticationpopups(playwright:Playwright):

    #approach 1
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={"username":"admin","password":"admin"})
    # page= context.new_page()

    # page.goto("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    # expect(page.locator("text=Congratulations! You must have the proper credentials."))
    # page.close

    # #Approach 2
    page1= context.new_page()
    page1.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page1.locator("text=Congratulations! You must have the proper credentials."))
    page1.close


def test_handletabs(playwright:Playwright):

    #approach 1
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    # page= context.new_page()

    # page.goto("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    # expect(page.locator("text=Congratulations! You must have the proper credentials."))
    # page.close

    # #Approach 2
    parentpage= context.new_page()
    parentpage.goto("https://testautomationpractice.blogspot.com")
    #register an event for handle tabs
    parentpage.on("page",lambda page:page.wait_for_load_state())
    parentpage.locator("button[onclick='myFunction()']").click()
    parentpage.wait_for_timeout(2000)

    pages=context.pages

    for page in pages:
        print(page.url)


    






        




 


