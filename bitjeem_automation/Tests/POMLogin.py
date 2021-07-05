# import email
import time
from selenium import webdriver
import unittest
from Page.POMHomePage import Homepage
from Page.POMLoginPage import LoginPage
from Page.POMRegisterPage import RegisterPage
import HTMLTestRunner
import pytest


class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/home/cinqtech/PycharmProjects/bitjeem_automation/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://qa.cinqtech.com/")
        time.sleep(5)

    def test_01_landing_on_bitjeem_page(self):
        driver = self.driver
        time.sleep(5)
        titleofwebpage = driver.title
        self.assertEqual("Protect Digital Assets, Digital Assets Safeguard - bitjeem.com", titleofwebpage)
        time.sleep(2)
        print("test 01 : landing on bitjeem page Passed")

    def test_02_landing_on_valid_page_before_login(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        time.sleep(3)
        home.click_login()
        titleofwebpage = driver.title
        self.assertEqual("bitjeem | login", titleofwebpage)
        time.sleep(2)
        print("test 02 : landing on login page after clicking the login button Passed")

    def test_03_login_valid_with_TFA(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        home.click_login()
        login.enter_useremail("muzammil1@cinqtech.com")
        login.enter_userpassword("system@123")
        login.click_login_button()
        time.sleep(3)
        login.twofactor_submit_button()
        time.sleep(5)
        home.click_usericon()
        home.click_logout_button()
        # driver.close()
        print("test 03 : login with valid user credentials as well as two factor authentication Passed.")

    def test_04_login_valid_without_TFA(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        home.click_login()
        login.enter_useremail("automationuser1@mailinator.com")
        login.enter_userpassword("system@123")
        login.click_login_button()
        time.sleep(5)
        home.click_usericon()
        home.click_logout_button()
        print("test 03 : login with valid user credentials but not two factor authentication Passed.")

    def test_05_landing_on_valid_page_after_login(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        home.click_login()
        login.enter_useremail("muzammil1@cinqtech.com")
        login.enter_userpassword("system@123")
        login.click_login_button()
        time.sleep(3)
        login.twofactor_submit_button()
        time.sleep(3)
        titleofwebpage = driver.title
        self.assertEqual("bitjeem | Dashboard", titleofwebpage)
        time.sleep(2)
        home.click_usericon()
        home.click_logout_button()
        print("test 04 : after login process landing on bitjeem dashboard Passed")

    def test_06_login_invalid_useremail(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        home.click_login()
        login.enter_useremail("automation_user1@mailinator.com")
        login.enter_userpassword("system@123")
        login.click_login_button()
        message = driver.find_element_by_xpath("/html/body/app-root/div/app-guest/section/app-login/section/div/div"
                                               "/div/form/div[1]/div[2]/p").text
        self.assertEqual(message, "Email or Password is incorrect.")
        print("test 05 : Login with invalid user credentials Passed.")

    def test_0_login_with_invalid_password(self):
        driver = self.driver
        home = Homepage(driver)
        login = LoginPage(driver)
        home.click_login()
        login.enter_useremail("automationuser2@mailinator.com")
        login.enter_userpassword("system@1234")
        login.click_login_button()
        invalid_password = driver.find_element_by_xpath(
            "/html/body/app-root/div/app-guest/section/app-login/section/div/div/div"
            "/form/div[2]/div[1]/ngb-popover-window/div[2]/p").text
        print(invalid_password)
        time.sleep(3)
        login.enter_userpassword("System@!123")
        login.click_login_button()
        invalid_password = driver.find_element_by_xpath(
            "/html/body/app-root/div/app-guest/section/app-login/section/div/div/div"
            "/form/div[2]/div[1]/ngb-popover-window/div[2]/p").text
        print(invalid_password)
        time.sleep(3)
        login.enter_userpassword("system@12")
        login.click_login_button()
        time.sleep(2)
        text_block_messeage = driver.find_element_by_xpath(
            "/html/body/app-root/div/app-guest/section/app-login/section/div/div/div/form/div[2]/div[3]/p").text
        print(text_block_messeage)
        self.assertEqual(text_block_messeage, "Your account has been locked")
        print("test 06 : Login with invalid password Passed.")

    # def test_05_register_valid(self):
    #     driver = self.driver
    #     home = Homepage(driver)
    #     reg = RegisterPage(driver)
    #     home.click_register_icon()
    #     time.sleep(3)
    #     reg.enter_firstname("test")
    #     reg.enter_lastname("muzzamiljaffri")
    #     reg.enter_phone_number("1111111111")
    #     reg.enter_email("muzzamil_jaffri@hotmail.com")
    #     reg.click_verify()
    #     time.sleep(5)
    #     reg.click_recaptcha_checkbox()
    #     time.sleep(15)
    #     phone_code = input('Enter the phone verification code: ')
    #     email_code = input('Enter the email verification code: ')
    #     reg.enter_mobileverificationcode(phone_code=phone_code)
    #     reg.enter_emailverificationcode(email_code=email_code)
    #     reg.enter_userpassword("system@123")
    #     reg.enter_confirm_password("system@123")
    #     reg.click_pp_button()
    #     reg.submit_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == 'main':
    unittest.main()
