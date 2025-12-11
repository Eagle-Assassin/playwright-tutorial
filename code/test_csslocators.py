import pytest
from playwright.sync_api import Page, expect
"""
tag id tag#id
tag class  tag.class
tag attribute tag[attribute=value]
tag class attribute tag.class[attribute=value]
"""

def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com")

    #A. CSS locators
    #1. tag  id
    page.locator("input#small-searchterms").fill("T-Shirts")
    #can also be written as -> page.locator("#small-searchterms").fill("T-Shirts")
    page.wait_for_timeout(2000)

    #2. Tag and Class
    page.locator("input.search-box-text").fill("Tag and class")
    #can also be written as -> page.locator(".search-box-text").fill("T-Shirts")
    page.wait_for_timeout(2000)

    #3. Tag and Attributes
    page.locator("input[name=q]").fill("tag and attribute")
    #Also written as page.locator("[name=Search store]").fill("tag and attribute")
    page.wait_for_timeout(2000)

    #4.tag class attribute
    page.locator("input.search-box-text[value='Search store']").fill("tag class attribute")
    page.wait_for_timeout(2000)