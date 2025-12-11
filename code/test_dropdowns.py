import pytest
from playwright.sync_api import Page, expect

def test_dropdowns(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    #1.Selct and option from the drop-down
    #Single select 3ways to selct option from the dropdown
    page.locator("select#country").select_option(label="India") #by label

    page.locator("select#country").select_option("germany") #by value

    page.locator("select#country").select_option(index=3) #by index , starts from 0

    #Check number of options in the dropdown

    dropdowns=page.locator("select#country>option")

    expect(dropdowns).to_have_count(10)

    options=[text.strip() for text in dropdowns.all_text_contents()]

    page.wait_for_timeout(2000)

    print(options)


    #Multi Selection option

    page.locator("select#colors").select_option(["Red","Blue","Green"]) #by label page.locator("select#colors").select_option(label =["Red","Blue","Green"])

    page.locator("select#colors").select_option(value=["red","white","green"])#by value case sensitive

    page.locator("select#country").select_option(index=[0,2,1,4]) #by index , starts from 0

    #Check the number of options


    page.wait_for_timeout(2000)

    dropdowns=page.locator("select#colors>option")

    expect(dropdowns).to_have_count(7)

    options=[text.strip() for text in dropdowns.all_text_contents()]

    page.wait_for_timeout(2000)


    # Check if the doropdown elements are sOrted or not
    unsorted=page.locator("select#colors>option") #by label page.locator("select#colors").select_option(label =["Red","Blue","Green"])
    sorted_values=page.locator("select#animals>option")

    sorted_list=sorted_values.all_text_contents()
    unsorted_list=unsorted.all_text_contents()
    elements_in_unsorted=[value.strip() for value in unsorted_list]
    elements_in_sorted=[value.strip()  for value in sorted_list]

    unsorted_copy=elements_in_unsorted.copy()
    sorted_copy=elements_in_sorted.copy()

    if  sorted(unsorted_copy)==elements_in_unsorted:
        print("The lists are Sorted")
        assert True
    else:
        print("The lists are Unsorted")
   
    if sorted(sorted_copy)==elements_in_sorted:
        print("The lists are Sorted")
        assert True
    else:
        print("The lists are Unsorted")



    