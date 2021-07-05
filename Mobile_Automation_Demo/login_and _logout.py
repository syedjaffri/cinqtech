import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "emulator-5554",
    "app": "/home/cinqtech/Downloads/bitjeem_qa_2.25.5.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

'''for login'''
time.sleep(10)
driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
time.sleep(4)
driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("muzammil1@cinqtech.com")
driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
# driver.hide_keyboard()
'''
Touch Actions for scrolling the page 
'''
TouchAction(driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()

time.sleep(5)
driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
time.sleep(5)
'''for logout'''

driver.find_element_by_id("com.bitjeem.android:id/btnLogout").click()
