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
'''for registration of new user'''
time.sleep(10)
driver.find_element_by_id('com.bitjeem.android:id/tvRegister').click()
driver.implicitly_wait(3)
driver.find_element_by_id('com.bitjeem.android:id/etFirstName').send_keys('Rehan')
driver.find_element_by_id('com.bitjeem.android:id/etLastName').send_keys('Raza')
driver.find_element_by_id('com.bitjeem.android:id/codeSpinner').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.LinearLayout[1]').click()
driver.find_element_by_id('com.bitjeem.android:id/etMobile').send_keys('111222333')
driver.find_element_by_id('com.bitjeem.android:id/etEmail').send_keys('rehan@mailinator.com')
driver.find_element_by_id('com.bitjeem.android:id/btnVerify').click()
time.sleep(2)
driver.find_element_by_id('com.bitjeem.android:id/reCaptchaCheck').click()
'''this delay is for captcha verification'''
time.sleep(30)
driver.find_element_by_id('com.bitjeem.android:id/btnContinue').click()
'''this delay is for entering the verification code of mobile and email'''
phone_verification_code = input('Enter mobile number verification code : ')
email_verification_code = input('Enter email verification code : ')
time.sleep(5)
driver.find_element_by_id('com.bitjeem.android:id/etMobileCode').send_keys(phone_verification_code)
driver.find_element_by_id('com.bitjeem.android:id/etEmailCode').send_keys(email_verification_code)
driver.hide_keyboard()
'''
Touch Actions for scrolling the page 
'''
# TouchAction(driver).press(x=717, y=1473).move_to(x=717, y=533).release().perform()
driver.find_element_by_id('com.bitjeem.android:id/etPassword').send_keys('system@123')
driver.find_element_by_id('com.bitjeem.android:id/etRePassword').send_keys('system@123')
driver.find_element_by_id('com.bitjeem.android:id/agreementCheck').click()
# driver.hide_keyboard()
time.sleep(2)
TouchAction(driver).press(x=462, y=989).move_to(x=462, y=516).release().perform()
driver.implicitly_wait(3)
driver.find_element_by_id('com.bitjeem.android:id/btnRegister').click()
time.sleep(3)
'''for logout'''
driver.find_element_by_id("com.bitjeem.android:id/btnLogout").click()
