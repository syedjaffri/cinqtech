# from selenium.webdriver.common.by import By
#
#
#
# # ---- Login page locators ---
# Login_Button_on_Navbar = (By.XPATH, "/html/body/app-root/div/app-header-guest/section[1]/nav/div/div/ul/li[2]/a")
# Email_address = (By.ID, "email")
# Password = (By.ID, "password")
# Login_Button = (By.ID, "login")
# TwoFactorAuth_Submit = (By.ID, "2faButton")
#
# #  ---- Registration Page Locators ----
# Registration_Button_on_Navbar = (By.XPATH, "/html/body/app-root/div/app-header-guest/section["
#                                            "1]/nav/div/div/ul/li[3]/a")
# First_Name = (By.ID, "fn")
# Last_Name = (By.ID, "ln")
# Phone_Number = (By.ID, "phone")
# # email address is same so no need to duplicate the locator
# Code_Verification = (By.ID, "code_email")
# Phone_verification_Code = (By.ID, "phone_num_code")
# Email_verification_Code = (By.ID, "vcode")
# # password attribute is also same as on login page locators
# Confirm_Password = (By.ID, "cp")
# Form_Check_Box = (By.ID, "form-check")
# Form_Submission = (By.XPATH, "/html/body/app-root/div/app-guest/section/app-register/section/div/div/div/form"
#                              "/button")
#
# #  ---- Forget Password ----
# # for forget password the user must be on the login screen
# Forget_password_Button = (By.XPATH, "/html/body/app-root/div/app-guest/section/app-login/section/div/div/div/form"
#                                     "/p[3]/a")
# # Enter the email Address
# Get_Code_Button = (By.XPATH, "/html/body/app-root/div/app-guest/section/app-forgot-password/section/section/div"
#                              "/div/div/form/div[2]/div/div/button")
# # Enter code that is provided via email under Email_verification_code
# # After entering code the user will need to enter the password and confirm the password as well.
# Set_Forget_Password = (By.XPATH, "/html/body/app-root/div/app-guest/section/app-forgot-password/section/section"
#                                  "/div/div/div/form/div[3]/button")