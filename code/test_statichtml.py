import pytest
from playwright.sync_api import Page, expect

#Static tables
def test_statictables(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    table=page.locator("table[name='BookTable'] tbody") #locate the whole table
    expect(table).to_be_visible() #Check visibility

    #Count the number of rows=
    print("pass")
    rows= page.locator("table[name='BookTable'] tbody tr") #which is equivalent to table.locator("tr")
    #Count the rows
    num_rowsintable=rows.count()

    #2.Count the number of columns/header in table
    now_of_cols=rows.locator("th").count()

    print(num_rowsintable,now_of_cols)

    #3. Read all the data from the second row of the table
    #we have already cpatured all the rows
    second_rowdata=rows.nth(1).locator("td")
    

    print(second_rowdata.all_inner_texts())

    expect(second_rowdata).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    #4. Read all the data from the table excluding the header
    all_row_data=rows.all() #This is returns thelist of locators

    print(all_row_data)
    for row in all_row_data[1:]:
        textofrows=row.locator("td").all_inner_texts()
        print(textofrows)

    #5.Conditional based printing-> print book name whose author is mukesh

    for row in all_row_data[1:]:
        authorname=row.locator("td").nth(1).inner_text()
        if authorname=='Mukesh':
            print("Book Name by {} is {}".format (authorname,row.locator("td").nth(0).inner_text()))

    #6. Find the total of the prices.
    total=0.0
    for row in all_row_data[1:]:
        price=row.locator("td").nth(-1).inner_text()
        total+=float(price)
    print("Total Price of all books is  {}".format (total))


    


