from playwright.sync_api import Page,expect


def test_verifypageurl(page:Page): # Playwright gives a built in fixture called page
    page.goto("http://www.automationpractice.pl/index.php") #passing url
    url=page.url #capture the Url of the page
    print("{} is the url".format(url))
    expect(page).to_have_url("http://www.automationpractice.pl/index.php") #this is used for page validation, this should be in the page

def test_verifytitlepage(page:Page):
    page.goto("http://www.automationpractice.pl/index.php") #passing url
    title= page.title()
    print("{} is the page title".format(title))
    expect(page).to_have_title("My Shop") #this is used for page validation, this should be in the page



