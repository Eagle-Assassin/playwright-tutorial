from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def test_simpledialogue(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

# Aproach 1
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog) #registering an event

    page.locator("#alertBtn").click() #Clicking on th ebutton whihc will open the dialogue

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_simpledialogue2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

#Approach 2 using Lamda function

    page.on("dialog",lambda dialog:dialog.accept()) #registering an event    #lambda parameter :expression
    page.wait_for_timeout(5000) 

    page.locator("#alertBtn").click() #Clicking on th ebutton whihc will open the dialogue

    page.wait_for_timeout(5000)


def test_confirmation(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    #Approach 2 using Lamda function

    page.on("dialog",lambda dialog:dialog.accept()) #Close the dialog usign accept button    #lambda parameter :expression
    # page.on("dialog",lambda dialog:dialog.dismiss()) #Close the dialog usign dismiss button
    # page.wait_for_timeout(5000) 

    page.locator("#confirmBtn").click() #Clicking on th ebutton whihc will open the dialogue

    # page.wait_for_timeout(5000)
    text= page.locator("#demo")
    expect(text).to_have_text("You pressed OK!")

def test_confirmation2(page:Page):

    page.goto("https://testautomationpractice.blogspot.com")
    page.on("dialog",lambda dialog:dialog.dismiss()) #Close the dialog usign dismiss button

    page.locator("#confirmBtn").click() #Clicking on th ebutton whihc will open the dialogue

    # page.wait_for_timeout(5000)
    text= page.locator("#demo")
    expect(text).to_have_text("You pressed Cancel!")


def test_prompt_alert(page:Page):

    page.goto("https://testautomationpractice.blogspot.com")
    page.on("dialog",lambda dialog:dialog.accept("Sandman")) #Close the dialog usign dismiss button

    page.locator("#promptBtn").click() #Clicking on th ebutton whihc will open the dialogue

    # page.wait_for_timeout(5000)
    text= page.locator("#demo")
    expect(text).to_have_text("Hello Sandman! How are you today?")












