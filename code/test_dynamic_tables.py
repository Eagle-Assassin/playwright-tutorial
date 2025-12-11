import pytest
from playwright.sync_api import Page,expect

@pytest.mark.skip
def test_dynamic_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    table=page.locator("#taskTable tbody")

    #grab all rows
    table_data=table.locator('tr').all() #get all rows of the table in list format

    for row in table_data:
        row_data=row.locator('td').nth(0).inner_text()

        if row_data=='Chrome':
            for lin_data in row.locator('td').all_inner_texts():
                if ('%' in lin_data)==True:
                    cpu_usage=lin_data  #This can be done using ->row.locator('td:has-text('%)').inner_text()
                    break
    
    expect(page.locator(".chrome-cpu")).to_contain_text(cpu_usage)
    page.wait_for_timeout(50)

    print("Cpu load of chrome {}".format(cpu_usage))

    #pagination table
    # Navigate to all the pages and pick all the data from the page.

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    page.set_viewport_size({"width": 1920, "height": 1080})

    has_morepages=True
    while has_morepages:
        rows=page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())
        next_button=page.locator("button[aria-label='Next']")
        is_next_enabled=next_button.get_attribute('class') # expected values are ['dt-paging-button disabled next',"dt-paging-button next"]

        if 'disabled' in is_next_enabled:
            has_morepages=False
        else:
            next_button.click()
        page.wait_for_timeout(500)

def test_pagefiltering(page:Page):

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    page.set_viewport_size({"width": 1920, "height": 1080})

    dropdown=page.locator("#dt-length-0")
    dropdown.select_option(label="25")

    rows=page.locator("#example tbody tr")
    expect(rows).to_have_count(25)

    page.wait_for_timeout(2000)


