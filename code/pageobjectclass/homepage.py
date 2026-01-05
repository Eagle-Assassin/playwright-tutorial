from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page

        #CSS selector targeting all product links under the product page
        self.product_list_locator= "div#tbodyid div.card  h4.card-title a"

        #Add to cart button exact macth usingtext
        self.add_tocart_button = page.locator('a:has-text("Add to cart")')

        #Cart link in top menu
        self.cart_link = page.locator("#cartur")
    
    def add_product_to_cart(self,product_name:str):
        products = self.page.locator(self.product_list_locator)
        count = products.count()

        for i in range(count):
            name= products.nth(i).text_content().strip()

            if name==product_name:
                products.nth(i).click()
                break

        self.page.on("dialog",lambda dialog:dialog.accept()) #handle dialog
        # self.page.wait_for_timeout(5000)
        self.add_tocart_button.click()
            

    def gotocart(self):

        self.cart_link.click()
