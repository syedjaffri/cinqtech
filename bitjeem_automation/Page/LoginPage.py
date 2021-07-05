# from selenium.webdriver.common.by import By
#
# from Page.BasePage import BasePage
# from configuration.config import TestData
#
#
# class LoginPage(BasePage):
#     """locators of the class"""
#     Login_Button_on_Navbar = (By.XPATH, "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[2]/a")
#     Email_address = (By.ID, "email")
#     Password = (By.ID, "password")
#     Login_Button = (By.ID, "login")
#     TwoFactorAuth_Submit = (By.ID, "2faButton")
#
#     """Constructor of the page class"""
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get(TestData.BASE_URL)
#
#
#     """Page Actions"""
#     """this is use to get the page title"""
#
#     def get_login_page_title(self, title):
#         return self.get_title(title)
#
#     """this is to check the login link"""
#
#     def is_login_button_exist(self):
#         return self.is_visable(self.Login_Button_on_Navbar)
#
#     """this is used to login"""
#
#     def do_login(self, username, password):
#         self.do_click(self.Login_Button_on_Navbar)
#         self.do_send_key(self.Email_address, username)
#         self.do_send_key(self.Password, password)
#         self.do_click(self.Login_Button)
#         self.do_click(self.TwoFactorAuth_Submit)
