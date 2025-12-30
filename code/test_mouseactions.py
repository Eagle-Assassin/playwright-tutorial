from playwright.sync_api import Page, expect
import pytest

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    pointme=page.locator(".dropbtn")

    pointme.hover()

    laptops=page.locator(".dropdown-content a").nth(1) #or page.locator(".dropdown-content a:nth-child(2)").hover()

    laptops.hover()

    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    button=page.locator(".context-menu-one")

    button.click(button='right') #perform the rightclick action

    # laptops=page.locator(".dropdown-content a").nth(1) #or page.locator(".dropdown-content a:nth-child(2)").hover()

    # laptops.hover()

    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_mouse_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    button=page.locator("button[ondblclick='myFunction1()']")

    button.dblclick() #perform the rightclick action

    field2=page.locator("#field2")


    expect(field2).to_have_value("Hello World!")
    # laptops=page.locator(".dropdown-content a").nth(1) #or page.locator(".dropdown-content a:nth-child(2)").hover()

    # laptops.hover()

    page.wait_for_timeout(2000)



def test_mouse_danddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    source=page.locator("#draggable")

    target=page.locator("#droppable")

    #Approach 1: Manual drag using hover
    #action1
    source.hover()
    page.wait_for_timeout(1000)
    #action2: down or click on the source
    page.mouse.down()
    page.wait_for_timeout(1000)
    #action3: hover over target
    target.hover()
    page.wait_for_timeout(1000)
    #action4: mouse up
    page.mouse.up()
    page.wait_for_timeout(1000)

    page.reload()
    #Approach 2:drag_to()

    source.drag_to(target)
    page.wait_for_timeout(1000)

