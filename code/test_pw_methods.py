import pytest
from playwright.sync_api import Page, expect

def test_methods(page:Page):
    page.goto("https://demowebshop.tricentis.com")

    products=page.locator(".product-title") #6 products

    #innertext vs textcontent
    print("innertext vs textcontent")
    for i in range(products.count()):
        print("inner text: {}".format(products.nth(i).inner_text())) #retruns actual text
        print("text content: {}".format(products.nth(i).text_content()),end="\n\n") #returns special character and spaces

        
    #All inner text and all text content

    print("All inner text and all text content")
    for i in range(products.count()):
        print("inner text: {}".format(products.all_inner_texts()[i])) #retruns actual text
        print("text content: {}".format(products.all_text_contents()[i]),end="\n\n") #returns special character and spaces


    print("All inner text: {}".format(products.all_inner_texts()))
    print("All text content: {}".format(products.all_text_contents()))
