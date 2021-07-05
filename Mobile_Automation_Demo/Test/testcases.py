import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "emulator-5554",
            "app": "/home/cinqtech/Downloads/bitjeem_qa_2.25.5.apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        cls.driver = driver
        cls.driver.implicitly_wait(3)

    def test_01_first_splash_screen(self):
        first_splash_screen = self.driver.current_activity
        print(first_splash_screen)
        time.sleep(2)
        self.assertEqual(".SplashActivity", first_splash_screen)
        print("test 01 : Splash screen passed")
        self.driver.close_app()
        time.sleep(3)

    def test_02_landing_on_registration_page(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/tvRegister").click()
        time.sleep(4)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(3)
        self.assertEqual(".NewRegistrationActivity", activity)
        print("test 04 : landing on registration page passed.")
        self.driver.close_app()
        time.sleep(2)

    def test_03_landing_on_valid_page_after_login(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("muzammil1@cinqtech.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
        '''        Touch Actions for scrolling the page        '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(5)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(3)
        self.assertEqual(".NewDashboardActivity", activity)
        print("test 05: landing on valid page after login passed")
        self.driver.close_app()
        time.sleep(3)

    def test_04_landing_on_TFA_screen(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("ana@mailinator.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
        '''        Touch Actions for scrolling the page        '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(5)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(5)
        self.assertEqual(".NewTwoFactorActivity", activity)
        print("test 06: landing on Two factor authentication screen after login passed")
        self.driver.close_app()
        time.sleep(3)

    def test_05_landing_on_bitjeem_landing_page(self):
        self.setUpClass()
        time.sleep(10)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".NewLandingActivity", activity)
        print("test 02: landing on bitjeem mobile landing page passed")
        self.driver.close_app()
        time.sleep(3)

    def test_06_landing_on_login_page(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(3)
        self.assertEqual(".NewLoginActivity", activity)
        print("test 03 : landing on login page passed.")
        self.driver.close_app()
        time.sleep(2)

    def test_07_login_valid_with_TFA(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("ana@mailinator.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
        '''        Touch Actions for scrolling the page        '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/tfa_view").send_keys("123456")
        time.sleep(5)
        '''for logout'''
        self.driver.find_element_by_id("com.bitjeem.android:id/btnLogout").click()
        self.driver.close_app()
        time.sleep(2)

    def test_08_login_valid_without_TFA(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("muzammil1@cinqtech.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
        '''        Touch Actions for scrolling the page        '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(5)
        '''     for logout      '''
        self.driver.find_element_by_id("com.bitjeem.android:id/btnLogout").click()
        self.driver.close_app()
        time.sleep(2)

    def test_09_login_with_invalid_password(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("muzammil1@cinqtech.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123123")
        '''         Touch Actions for scrolling the page         '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(3)
        validation = self.driver.find_element_by_id("com.bitjeem.android:id/tvError").text
        '''for checking the assertion is true or flase'''
        self.assertEqual("Email or Password is incorrect.", validation)
        print("test 09: login with incorrect password.")
        self.driver.close_app()
        time.sleep(2)

    def test_10_login_invalid_useremail(self):
        self.setUpClass()
        time.sleep(10)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(4)
        self.driver.find_element_by_id("com.bitjeem.android:id/etEmail").send_keys("muzammil123@cinqtech.com")
        self.driver.find_element_by_id("com.bitjeem.android:id/etPassword").send_keys("system@123")
        '''         Touch Actions for scrolling the page         '''
        self.driver.hide_keyboard()
        # TouchAction(self.driver).press(x=717, y=1098).move_to(x=717, y=489).release().perform()
        time.sleep(5)
        self.driver.find_element_by_id("com.bitjeem.android:id/loginBtn").click()
        time.sleep(3)
        validation = self.driver.find_element_by_id("com.bitjeem.android:id/tvError").text
        '''for checking the assertion is true or flase'''
        self.assertEqual("Email or Password is incorrect.", validation)
        print("test 10: login with incorrect email.")
        self.driver.close_app()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")


if __name__ == 'main':
    unittest.main()
