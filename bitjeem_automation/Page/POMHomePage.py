from locators import locators


class Homepage:

    def __init__(self, driver):
        self.driver = driver

        self.login_button_xpath = locators.Locators.login_button_xpath
        self.user_icon_xpath = locators.Locators.user_icon_xpath
        self.logout_button_xpath = locators.Locators.logout_button_xpath
        self.regiter_button_xpath = locators.Locators.register_button_xpath

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_usericon(self):
        self.driver.find_element_by_xpath(self.user_icon_xpath).click()

    def click_logout_button(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

    def click_register_icon(self):
        self.driver.find_element_by_xpath(self.regiter_button_xpath).click()