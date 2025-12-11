import pytest
from playwright.sync_api import Page,expect

def test_input(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    text_box=page.locator("#name")

    #check the visibility and enability
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #verify the attribute
    expect(text_box).to_have_attribute("maxlength","15")

    #capture the value of the attribute
    maxlenth=text_box.get_attribute("maxlength")

    print( maxlenth)

    #Fil the text
    text_box.fill("abc")

    #Capture the input value from input box
    print("The value entered is {}".format(text_box.input_value()))


    page.wait_for_timeout(2000)

    #radio button and checkboxes
    male_radio=page.locator("#male")

    #check the visibility and enability
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    #verify if checked or not
    expect(male_radio).not_to_be_checked()

    #Check the radio button
    male_radio.check()

    #verify if checked
    expect(male_radio).to_be_checked()

    page.wait_for_timeout(2000)


    #Check box
    #Select a specific checkbox

    sunday_checkbox=page.get_by_label("Sunday")

    sunday_checkbox.check()

    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    #Count the total number of check boxes
        #step 1
    days= ['Sunday',"Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday']


    checkboxes=[page.get_by_label(day) for day in days]
    print("Total number of checkboxes".format(len(checkboxes)))


    #Check all checkboxes in one go and assert each check boxes
    for box in checkboxes:
        box.check()
        expect(box).to_be_checked()

    page.wait_for_timeout(2000)



    #Check last 3 check boxes
    for box in checkboxes:
        box.uncheck()
        expect(box).not_to_be_checked()

    for box in checkboxes[-3:]:
        box.check()
        expect(box).to_be_checked()


    page.wait_for_timeout(2000)

    #Check the unchecked and uncheck the checked check boxes

    for box in checkboxes:
        if (box.is_checked()):
            box.uncheck()
            expect(box).not_to_be_checked()
        elif not (box.is_checked()):
            box.check()
            expect(box).to_be_checked()
        page.wait_for_timeout(500)

    




