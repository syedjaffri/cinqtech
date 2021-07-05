from locators import locators


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.firstname_textbox_id = locators.Locators.firstname_textbox_id
        self.lastname_textbox_id = locators.Locators.lastname_textbox_id
        self.phone_number_textbox_id = locators.Locators.mobile_number_textbox_id
        self.email_textbox_id = locators.Locators.email_textbox_id
        self.verify_mobile = locators.Locators.code_email_button_id
        self.mobileverificationcode_textbox_id = locators.Locators.mvc_textbox_id
        self.emailverificationcode_textbox_id = locators.Locators.evc_textbox_id
        self.password_text_id = locators.Locators.password_textbox_id
        self.confirmpassword_textbox_id = locators.Locators.cp_textbox_id
        self.formcheck_checkbox_id = locators.Locators.pp_checkbox_id
        self.submit_button_xpath = locators.Locators.register_button_xpath
        self.recaptcha_checkbox_xpath = locators.Locators.verify_xpath

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)

    def enter_phone_number(self, number):
        self.driver.find_element_by_id(self.phone_number_textbox_id).send_keys(number)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def click_verify(self):
        self.driver.find_element_by_id(self.verify_mobile).click()

    def enter_mobileverificationcode(self, phone_code):
        # self.driver.find_element_by_id(self.mobileverificationcode_textbox_id).clear()
        self.driver.find_element_by_id(self.mobileverificationcode_textbox_id).send_keys(phone_code)

    def enter_emailverificationcode(self, email_code):
        self.driver.find_element_by_id(self.emailverificationcode_textbox_id).clear()
        self.driver.find_element_by_id(self.emailverificationcode_textbox_id).send_keys(email_code)

    def enter_userpassword(self, password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def enter_userpassword(self, password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def enter_confirm_password(self, cp):
        self.driver.find_element_by_id(self.confirmpassword_textbox_id).clear()
        self.driver.find_element_by_id(self.confirmpassword_textbox_id).send_keys(cp)

    def click_pp_button(self):
        self.driver.find_element_by_id(self.formcheck_checkbox_id).click()

    def submit_button(self):
        self.driver.find_element_by_id(self.submit_button_xpath).click()

    def click_recaptcha_checkbox(self):
        self.driver.find_element_by_xpath(self.recaptcha_checkbox_xpath).click()
