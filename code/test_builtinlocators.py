from playwright.sync_api import Page,expect
import re #regular expression
import time


#get_by_alt_text
def test_verify_pwlocators(page:Page):

    #1.  get by get_by_alt_text
    page.goto("https://demo.nopcommerce.com/")
    logo = page.get_by_alt_text("nopCommerce demo store") #this can be used to locate images on the webpage      

    #Check if the logo is visible
    expect(logo).to_be_visible() 

    #2. get _by_text-> visible text content
    text = page.get_by_text("Welcome to our store")  #Full text
    text1 = page.get_by_text("Welcome to our store")  #Partial text
    text2 = page.get_by_text(re.compile(".*Welcome.*")) #regular expression

    expect(text).to_be_visible() 
    expect(text1).to_be_visible() 
    expect(text2).to_be_visible() 


    #3. get by role
    path ='https://demo.nopcommerce.com/register?returnUrl=%2F'
    page.goto(str(path))
    time.sleep(4)

    role=page.get_by_role(role="heading",name="Register")

    expect(role).to_be_visible()

    #4. page.get_bylabel
    page.get_by_label('First Name:').fill("john")
    page.get_by_label("Last Name:").fill("kenedy")
    page.get_by_label("Email").fill("abc@gmail.com")
    #get by label

    time.sleep(2)

    #5. Get by place holder -> we can see something on the page once you type something it will disappear
    page.get_by_placeholder("Search Store").fill("Apple Macbook")
    page.wait_for_timeout(5000)


    #6. get by Title
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    element =page.get_by_title("Home Page Link")

    expect(element).to_have_text("Home")

    element1 =page.get_by_title("HyperText Markup Language")

    expect(element1).to_have_text("HTML")

    #6. get by test id

    testid = page.get_by_test_id("profile-name")

    expect(testid).to_have_text("John Doe")

    testemail= page.get_by_test_id("profile-email")

    expect(testemail).to_have_text("john.doe@example.com")






    page.close()


