import pytest
from playwright.sync_api import Page, expect
import re

def test_dynamictest(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Single xpath should handle the dynamic xpath -
    # -> Do not hardcode th elements  
    #1. Or operator
    #    -> //button[text()='start or text()='stop']
    # //button[@name='start' or @name'stop']

    #2. Using Contains function

    # //button[contains@(name,'st')]

    #3. Starts with

    # //button[starts-with(@name,'st')]

    for i in range(0,5):
        button=page.locator("//button[@name='start' or @name='stop']")
        button.click()
        page.wait_for_timeout(2000)

    #B. Handle using CSS
        #button[name='start'] , button[name='stop']

    for i in range(0,5):
        button=page.locator("button[name='start'] , button[name='stop']")
        button.click()
        page.wait_for_timeout(2000)

    #We can also use the * operator

    #playwright built in locator , we should use regular expression
    for i in range(0,5):
        button=page.get_by_role("button",name=re.compile("st.*"))
        button.click()
        page.wait_for_timeout(2000)

