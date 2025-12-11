from playwright.async_api import Page,expect,async_playwright
import pytest

@pytest.mark.asyncio
async def test_verifypageurl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        mypage=await browser.new_page()
        await mypage.goto("http://www.automationpractice.pl/index.php")
        await expect(mypage).to_have_url("http://www.automationpractice.pl/index.php") #this is used for page validation, this should be in the page
