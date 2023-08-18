from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()

# accept cookies
driver.get("https://www.monkeytype.com")
popups = driver.find_element(By.ID, "popups")
cookiePopup = popups.find_element(By.ID, "cookiePopup")
main = cookiePopup.find_element(By.CLASS_NAME, "main")
buttons = main.find_element(By.CLASS_NAME, "buttons")
button = buttons.find_element(By.CLASS_NAME, "acceptAll")
button.click()

time.sleep(2)

# find words list
app = driver.find_element(By.ID, "app")
centerContent = app.find_element(By.ID, "centerContent")
middle = centerContent.find_element(By.ID, "middle")
active = middle.find_element(By.CLASS_NAME, "active")
typingTest = active.find_element(By.ID, "typingTest")
wordsWrapper = typingTest.find_element(By.ID, "wordsWrapper")
words = wordsWrapper.find_element(By.ID, "words")

# write every active word followed by space.
# finds word before typing so should be slower when compared to
# scrapping entire list before typing the list out.
try:
    while (1):
        activeWord = words.find_element(By.CLASS_NAME, "active")
        pyautogui.write(activeWord.text)
        pyautogui.press("space")
except:
    time.sleep(60)  # take your screenshots

driver.quit()
