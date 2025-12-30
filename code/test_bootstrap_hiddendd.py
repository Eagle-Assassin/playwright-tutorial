import pytest
from playwright.sync_api import Page, expect

#Boot strap dropdown would not have a select tab. The drop-downs woul be auto select type ahead search

def test_bootstrap_dropdowns(page:Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #login Step
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()

    #Click on PIM
    page.get_by_text("PIM").click()

    #Click on the job title drop-down
    page.locator("form i").nth(2).click() #open the options

    page.wait_for_timeout(3000)

    #how to write code to select the options -> the the DOM frosen from sources to capture the css
    options=page.locator("div[role='listbox'] span")

    count= options.count()
    print("Number of options in the dropdown {}".format(count))

    expect(options).to_have_count(count)

    # print(options.all_text_contents())
    page.wait_for_timeout(3000)

    #Print all the options using loop
    for i in range(count):
        print(options.all_text_contents()[i])

    #Select/click option from the drop-down - Cannot use select option
    for i in range(count):
        text= (options.all_text_contents()[i])
        if text=='Automaton Tester':
            options.nth(i).click()
            break
    page.wait_for_timeout(2000)


    








