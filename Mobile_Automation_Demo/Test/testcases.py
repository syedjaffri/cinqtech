import HtmlTestRunner
import xmlrunner
import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "294a638c7b3f7ece",
            "app": "/home/cinqtech/Downloads/build_0_27_2_ChangeId.apk",
            "systemPort": "2810"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        cls.driver = driver

    def test_01_login_valid_without_TFA(self):
        # self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.ListView"
                                                    "/android.widget.RelativeLayout[3]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(2)
        self.driver.close_app()
        time.sleep(2)

    def test_02_landing_on_valid_page_after_login(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.ListView"
                                                    "/android.widget.RelativeLayout[3]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(3)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".DashboardActivity", activity)
        print("test 02: landing on valid page after login passed")
        self.driver.close_app()
        time.sleep(2)

    def test_03_login_valid_with_TFA(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        # TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.ListView'
                                                    '/android.widget.RelativeLayout[1]').click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/tfa_view").send_keys("123456")
        time.sleep(2)
        self.driver.close_app()
        time.sleep(2)

    def test_04_landing_on_TFA_screen(self):
        self.setUpClass()
        time.sleep(6)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        # TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.ListView"
                                                    "/android.widget.RelativeLayout[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(3)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".TwoFactorActivity", activity)
        print("test 04: landing on Two factor authentication screen after login passed")
        self.driver.close_app()
        time.sleep(2)

    def test_05_login_invalid_useremail(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.ListView"
                                                    "/android.widget.RelativeLayout[3]").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/etEmail").clear().send_keys("muzzamil"
                                                                                                     "@cinqtech.com")
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(2)
        validation = self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/tvError").text
        '''for checking the assertion is true or false'''
        self.assertEqual("Email or Password is incorrect.", validation)
        print("test 05: login with incorrect email.")
        self.driver.close_app()
        time.sleep(2)

    def test_06_login_with_invalid_password(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        TouchAction(self.driver).press(x=507, y=981).move_to(x=507, y=808).release().perform()
        self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.ListView"
                                                    "/android.widget.RelativeLayout[3]").click()
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/etPassword").clear().send_keys("system@12345")
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_login").click()
        time.sleep(2)
        validation = self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/tvError").text
        '''for checking the assertion is true or false'''
        self.assertEqual('Email or Password is incorrect.\nYou have 2 attempts remaining.', validation)
        print("test 06: login with incorrect password.")
        self.driver.close_app()
        time.sleep(2)

    def test_07_landing_on_login_page(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/loginBtn_landing").click()
        time.sleep(2)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".LoginActivity", activity)
        print("test 07 : landing on login page passed.")
        self.driver.close_app()
        time.sleep(2)

    def test_08_first_splash_screen(self):
        self.setUpClass()
        first_splash_screen = self.driver.current_activity
        print(first_splash_screen)
        time.sleep(2)
        self.assertEqual(".SplashActivity", first_splash_screen)
        print("test 08 : Splash screen passed")
        self.driver.close_app()
        time.sleep(2)

    def test_09_landing_on_registration_page(self):
        self.setUpClass()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value="com.bitjeem.android:id/tvRegister_landing").click()
        time.sleep(2)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".RegistrationActivity", activity)
        print("test 09 : landing on registration page passed.")
        self.driver.close_app()
        time.sleep(2)

    def test_10_landing_on_bitjeem_landing_page(self):
        self.setUpClass()
        time.sleep(5)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.assertEqual(".LandingActivity", activity)
        print("test 10 : landing on bitjeem mobile landing page passed")
        self.driver.close_app()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("test completed")


# html_report_dir = './Reports/HTML_Reports'
# xml_report_dir = './Reports/XML_Reports'
#
#
# def run_all_test():
#     unittest.main()
#
#
# # Run all test function and generate html report.
# def run_all_test_generate_html_report():
#     # Run all test functions with HtmlTestRunner to generate html test report.
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
#
#
# # Run all test function and generate html report.
# def run_all_test_generate_xml_report():
#     # Run all test functions with HtmlTestRunner to generate html test report.
#     unittest.main(testRunner=xmlrunner.XMLTestRunner(output=xml_report_dir))
#
#
# def run_all_test_in_class_generate_html_report(test_case_class):
#     # Create a TestSuite object.
#     test_suite = unittest.TestSuite()
#     # Make all test function
#     test = unittest.makeSuite(test_case_class)
#     test_suite.addTest(test)
#     # Create HtmlTestRunner object and run the test suite.
#     test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
#     test_runner.run(test_suite)
#
#
# # Run all test functions in the specified test case class, the function parameter must be a class name not the class
# # name string.
# def run_all_test_in_class_generate_xml_report(test_case_class):
#     # Create a TestSuite object.
#     test_suite = unittest.TestSuite()
#     # Make all test function
#     test = unittest.makeSuite(test_case_class)
#     test_suite.addTest(test)
#     # Create HtmlTestRunner object and run the test suite.
#     test_runner = xmlrunner.XMLTestRunner(output=xml_report_dir)
#     test_runner.run(test_suite)


if __name__ == 'main':
    # run_all_test()
    unittest.main()
