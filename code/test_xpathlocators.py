import pytest
from playwright.sync_api import Page, expect
'''
#Xpath stands for XML Path Language
1. Absolute Xpath
2. Relative Xpath


This  also works on DOM Document Object Model


'''

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com")

    #1.Absolute Xpath - Not recommended
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()
    page.wait_for_timeout(2000)

    #2.Relative Xpath //tagname[@attribute='value']

    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(2000)

    #3. Xpath with contains - Dynamic elements

    products=page.locator("//h2//a[contains(@href,'computer')]")
    print("{} are presents ".format(products.count()))

    expect(products).to_have_count(products.count())
    

    #capture the first product text
    first= products.first.text_content()#get the text 

    print("Value of first Text ->{}".format(products.first.text_content())) #First
    print("Value of last Text ->{}".format(products.last.text_content()))  #last
    print("Value of Nth Text  ->{}".format(products.nth(2).text_content()))#nth

    #get the all text content
    for product,i in enumerate(products.all_text_contents()):
         print("Value of {} Text  ->{}".format(product,i))#nth

    #Xpath with starts with
    buld_products=page.locator("//h2//a[starts-with(@href,'/build')]")
    print("products start with build {}".format(buld_products.count()))

    expect(buld_products).to_have_count(buld_products.count())


    #inner text
    registration_link=page.locator("//a[text()='Register']")

    expect(registration_link).to_be_visible()

    #Xpath with last function
    google_plus_link=page.locator("//div[@class='column follow-us']//li[last()]")  #thiss will give the google plus link

    expect(google_plus_link).to_have_text("Google+")

    #Xpath with position

    twitter_link=page.locator("//div[@class='column follow-us']//li[position()=2]")  #thiss will give the google plus link

    expect(twitter_link).to_have_text("Twitter")











