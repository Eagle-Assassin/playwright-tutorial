from playwright.sync_api import Playwright,expect,Page
import pytest
import time
import datetime
#approach1
@pytest.mark.skip
def test_videoandss(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768}
    )

    page=context.new_page()
    
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    # expect(page.locator("#logout2")).to_be_visible()
    # expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')

    context.close() #Always needed to be closed to record the video
    browser.close() #Always needed to be closed to record the video
@pytest.mark.skip
def test_ss(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768}
    )

    page=context.new_page()
    
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    # expect(page.locator("#logout2")).to_be_visible()
    # expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')

    context.close() #Always needed to be closed to record the video
    browser.close() #Always needed to be closed to record the video

@pytest.mark.skip
def test_screenshot(page:Page):

    current_time=time.time()
    current_time1= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    page.goto("https://demowebshop.tricentis.com")

    #Page Screenshot(partially/visible)s
    path ="screenshots/homepage"+str(current_time1)+".jpg"
    page.screenshot(path=path)

    #Full Page Screenshot
    current_time1= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path ="screenshots/homepage"+str(current_time1)+".jpg"
    page.screenshot(path=path,full_page=True)


    #Element/specific section of the page
    current_time1= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path ="screenshots/homepage"+str(current_time1)+".jpg"
    logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=path)


    #Feature products
    current_time1= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path ="screenshots/homepage"+str(current_time1)+".jpg"
    products = page.locator(".product-grid.home-page-product-grid")
    products.screenshot()

@pytest.mark.skip
#Capture the trace-> Need a browser context
def test_trace(playwright:Playwright):
    browser = playwright.chromium.launch(headless= False)
    context= browser.new_context()

    #Starting the trace
    context.tracing.start(screenshots=True,snapshots=True)

    page= context.new_page()

    page.goto("https://www.demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")

    #Stopping the trace
    context.tracing.stop(path ="trace/trace.zip")

    context.close()
    browser.close()


#Auto Retry
#test Failed -> Flaky Test ( sometimes pass and sometimes fail) code-->pytest -s -v --reruns-delay 2 --headed ./test_handlescreeshotvideostraceviwerflake.py
#We need another library pytest-rerunfailues
def  test_autoretry(page:Page):
    page.goto("https://www.demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(5000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")