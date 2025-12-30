from playwright.sync_api import Page, expect
import pytest

def test_keyboard_action(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    input1=page.locator("#input1")
    #Focus on input1
    input1.focus()

    #2.Provide the step in input1
    page.keyboard.insert_text("Welcome")

    page.wait_for_timeout(2000)
    #Cntrl+a
    page.keyboard.press("Control+A")

    page.wait_for_timeout(2000)

    #Cntrl+C
    page.keyboard.press("Control+C")

    #Press tab two times

    for i in range(0,2):
        page.keyboard.press("Tab")
        page.wait_for_timeout(2000)


    #Cntrl+V-> Paste the text in the second box
    page.keyboard.press("Control+V")
    page.wait_for_timeout(2000)

    for i in range(0,2):
        page.keyboard.press("Tab")
    
    


    #Cntrl+V-> Paste the text in the third box
    page.keyboard.press("Control+V")
    page.wait_for_timeout(2000)


    #Caputre input2 and 3
    input2=page.locator("#input2")
    input3=page.locator("#input3")

    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")
    page.wait_for_timeout(2000)



