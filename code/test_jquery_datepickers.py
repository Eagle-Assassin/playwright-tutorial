from playwright.sync_api import Page,expect
import pytest



def selectdate(page,year,month,day,is_future):

    if  is_future:
        go=page.locator(".ui-datepicker-next")
    else:
        go=page.locator(".ui-datepicker-prev")

    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()

        print(current_month,current_year ,month,year)
        if str(current_month).strip()==month and str(current_year).strip()==year:
            #Capture all the dates
            all_dates= page.locator(".ui-datepicker-calendar td").all()
            for dt in all_dates:
                # print("test")
                if dt.inner_text()==day:
                    print(dt.inner_text())
                    dt.click()
                    return ("Pass")
        else:
            go.click()
    



@pytest.mark.skip
def test_jquert(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")
    dateinput=page.locator("#datepicker")

    #Approach 1
    
    # dateinput.fill("10/15/2025")  #dd/mm/yyyy

    #Approach 2 - User deined function

    dateinput.click()

    is_future=True
    out=selectdate(page,"2029","October","15",is_future)

    print("Selected Date: {} and result {}".format("",out))

    expect(dateinput).to_have_value("10/15/2029")

    page.wait_for_timeout(5000)


def month_to_num(month):
    months = {
        "January": 1, "February": 2, "March": 3,
        "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "December": 12
    }
    return months[month]



def select_checkin_date(page,year,month,day):  
     
    while True:
        to_select_checkin_date=page.locator("h3[aria-live='polite']").nth(0)
        selected_month,selected_year=to_select_checkin_date.inner_text().split()

        # print(selected_year,selected_month)
        if str(selected_year)==year and str(selected_month)==month:
            picked_date=page.locator(".b8fcb0c66a").nth(0).locator("td").all()
            for dat in picked_date:
                if dat.inner_text()==day:
                    dat.click()
            break
        
        else:
            page.locator("button[aria-label='Next month']").click()


def select_checkout_date(page,year,month,day):
         
    while True:
        to_select_checkin_date=page.locator("h3[aria-live='polite']").nth(1)
        selected_month,selected_year=to_select_checkin_date.inner_text().split()

        print(selected_year,selected_month)
        if str(selected_year)==year and str(selected_month)==month:
            picked_date=page.locator(".b8fcb0c66a").nth(1).locator("td").all()
            # for dat in picked_date:
            #     # print('pass')
            #     if dat.inner_text()==day:
            #         # print("dat:{dat}".format(dat))
            #          # Click the date directly
            date_str = f"{year}-{month_to_num(month):02d}-{int(day):02d}"
            page.locator(f'[data-date="{date_str}"]').click()
            break
        
        else:
            page.locator("button[aria-label='Next month']").click()


def test_bootstrapdates(page:Page):
    page.goto("https://www.booking.com/")

    # page.wait_for_timeout(100000)
    page.get_by_role("button", name="Dismiss sign in information.").click()
    print("Pass")
    page.get_by_test_id("searchbox-dates-container").click()


    select_checkin_date(page,"2026",'January','20')
    select_checkout_date(page,"2026",'March','10')

    # page.get_by_test_id("date-display-field-start").click()
    checkin_date=page.get_by_test_id("date-display-field-start").inner_text()
    check_out_date=page.get_by_test_id("date-display-field-end").inner_text()


    print("Check-In date {} and checkout date {}".format(checkin_date,check_out_date))


    expect(page.get_by_test_id("date-display-field-start")).to_contain_text(checkin_date)
    expect(page.get_by_test_id("date-display-field-end")).to_contain_text(check_out_date)

