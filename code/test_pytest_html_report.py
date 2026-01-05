"""
Docstring for code.test_pytest_html_report

step 1: Install the plug in 
step 2: Configure pytest.ini

          addopts=--headed 
        --browser=chromium 
        --video=retain-on-failure 
        --screenshot=on 
        --tracing=retain-on-failure 
        --html=myreport.html --self-contained-html --capture=tee-sys
step 3: Attach Screenshot on Test Failures (conftest.py)
step 4: Create Sample Tests
step 5: Run the Test and generate the report
step 6: Attach Screenshot on Test Failures
"""

from playwright.sync_api import Page,expect

def test_url(page:Page):
    page.goto('https://demoblaze.com/index.html')
    expect(page).to_have_url('https://demoblaze.com/index.html')

def test_title(page:Page):
    page.goto('https://demoblaze.com/index.html')

def test_google_search(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_ging_search(page:Page):
    page.goto("https://www.bing.com")
    expect(page).to_have_title("Bing123")





























