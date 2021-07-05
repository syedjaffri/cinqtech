from locators import locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = locators.Locators.email_textbox_id
        self.password_textbox_id = locators.Locators.password_textbox_id
        self.login_button_id = locators.Locators.login_button_id
        self.twofactor_button_id = locators.Locators.twofactor_button_id
        self.invalid_useremail_message_xpath = "/html/body/app-root/div/app-guest/section/app-login/section/div/div" \
                                               "/div/form/div[1]/div[2]/p "

    def enter_useremail(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_userpassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def twofactor_submit_button(self):
        self.driver.find_element_by_id(self.twofactor_button_id).click()

    def check_invalid_useremail_message(self, msg):
        msg = self.driver.find_element_by_xpath(self.invalid_useremail_message_xpath).text
        return msg
