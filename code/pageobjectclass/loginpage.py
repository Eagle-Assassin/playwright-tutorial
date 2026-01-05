from playwright.sync_api import Page, expect
import pytest

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        #login link on home page
        self.login_link=self.page.locator("#login2")

        #username element
        self.user_input=self.page.locator("#loginusername")

        #password element
        self.password_input=page.locator("#loginpassword")

        #Login button after entering the credentials
        self.login_buttona =page.locator("button[onclick='logIn()']")
    
    #Action method
    def click_login_link(self):
        self.login_link.click()
    
    def enter_username(self,username):
        self.user_input.fill("") #Clear the input box
        self.user_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill("") #Clear the input box
        self.password_input.fill(password)

    def login_button(self):
        self.login_buttona.click()

    def perform_login(self,username,password):
        self.login_link.click()
        self.user_input.fill("") #Clear the input box
        self.user_input.fill(username)
        self.password_input.fill("") #Clear the input box
        self.password_input.fill(password)
        self.login_button.click()
