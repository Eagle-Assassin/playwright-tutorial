from playwright.sync_api import Page,expect
import pytest
import os

@pytest.mark.skip
def test_fileupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    #uploading Single file
    page.locator("#singleFileInput").set_input_files("/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Files_to_upload/Notes.txt")  #give the path of the file to upload

    #Click on upload
    page.locator("button:has-text('Upload Single File')").click()

    page.wait_for_timeout(2000)
    expect(page.locator("#singleFileStatus")).to_contain_text("Notes.txt")

@pytest.mark.skip
def test_multifileupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com")

    #uploading Multiple file
    files=["/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Files_to_upload/config.sh", 
           "/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Files_to_upload/env.sh" , 
           "/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Files_to_upload/Notes.txt" ,
           "/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Files_to_upload/run.sh"]
    page.locator("#multipleFilesInput").set_input_files(files)  #give the path of the file to upload

    #Click on upload
    page.locator("button:has-text('Upload Multiple Files')").click()

    page.wait_for_timeout(2000)
    expect(page.locator("#multipleFilesStatus")).to_contain_text("Notes.txt")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("env.sh")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("config.sh")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("run.sh")


def test_download(page:Page):

    # def handle_download(download):
    #     download.save_as("/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/code/Download/testfile.txt")

    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("This is to download a file")

    page.locator("#generateTxt").click() #This  will generate the link to download the file

    # page.on("download",handle_download)
    page.on("download",lambda download:download.save_as(
        "/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Download/testfile.txt"))

    page.locator("#txtDownloadLink").click()
    
    page.wait_for_timeout(5000)

    if os.path.exists("/home/section/Desktop/Files/MTECH IIT/Git projects/Projects/playwright-tutorial/code/Download/testfile.txt"):
        print("File Exits")
    else:
        print("File does not exist")










    

    