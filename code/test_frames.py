from playwright.sync_api import Page,expect
import pytest
@pytest.mark.skip
def test_frames1(page:Page):
    page.goto("https:ui.vision/demo/webtest/frames")
    
    frames=page.frames

    print("Number of frames are :{}".format(len(frames)))

    #frame 1 (grab the specific frame element) Option1
    frame1= page.frame_locator("frame[src='frame_1.html']") #get the frame 1

    frame1.locator("input[name=mytext1]").fill("Welcome")

    page.wait_for_timeout(5000)


    #Option 2

    frame1= page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html") #get the frame 1 by Url

    inputbox=frame1.locator("input[name=mytext1]")
    inputbox.fill("Welcome2")

    expect(inputbox).to_have_value("Welcome2")

    page.wait_for_timeout(5000)

    #Option 3 # get the frame using the name -> so we cant use here as we dont have any frame name here

    #wORKING WITH iNNER iFRAME

def test_inner_frames(page:Page):

    page.goto("https:ui.vision/demo/webtest/frames")

    #frame 3 (grab the specific frame element) Option1
    frame3= page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html") #get the frame 1

    frame3.locator("input[name='mytext3']").fill("Fill the text box")

    #Count the number of child frames

    child_frames= frame3.child_frames

    print("Number of child frames under frames3 are :{}".format(len(child_frames)))

    inner_frame = child_frames[0]

    radio = inner_frame.get_by_label("I am a human")
    radio.check()

    expect(radio).to_be_checked()





    

