from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

#initialize webdriver for chrome
driver = webdriver.Chrome()

#starting the browser
url = "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.kennesaw.edu%2Fccse%2Ffirst-year-experience%2Fcse1322%2Fslides%2Fm4.2-recursion1.pptx&wdOrigin=BROWSELINK"
driver.get(url)

#starting screenshot number
screenShotNumber = 0

def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    print(f"Screenshot saved as {file_name}")


while True:
        # Check for key press to take screenshot
        if keyboard.is_pressed('s'):
            file_name = (f"ScreenShot#{screenShotNumber}.png")
            take_screenshot(driver, file_name)
            screenShotNumber += 1

        # Check for key press to exit the script
        if keyboard.is_pressed('q'):
            print("Exiting the script.")
            break

driver.quit()

