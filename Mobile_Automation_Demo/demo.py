import unittest
from appium import webdriver


class LocalAndroidTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Quick Start Android Native Demo'
    accessKey = "eyJhbGciOiJIUzI1NiJ9.eyJ4cC51IjoxMjA2NjU2MywieHAucCI6MTIwNjY1NjIsInhwLm0iOjE2MjUwNDMzNzQ2OTgsImV4cCI6MTk0MDQwMzQxMCwiaXNzIjoiY29tLmV4cGVyaXRlc3QifQ.QUW0XfEvfq114Bw5KQWw280qVXCw_7xkNKvsFwo-Y4I"
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['accessKey'] = self.accessKey
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.dc['platformName'] = 'android'
        self.dc['deviceQuery'] = "@os='android' and @version='9' and @category='PHONE'"
        self.driver = webdriver.Remote("https://cloud.seetest.io/wd/hub", self.dc)

    def testQuickStartAndroidNativeDemo(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='usernameTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@id='passwordTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='Login']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Make Payment']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='phoneTextField']").send_keys('1234567')
        self.driver.find_element_by_xpath("xpath=//*[@id='nameTextField']").send_keys('Jon Snow')
        self.driver.find_element_by_xpath("xpath=//*[@id='amountTextField']").send_keys('50')
        self.driver.find_element_by_xpath("xpath=//*[@text='Select']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Switzerland']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Send Payment']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Yes']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Logout']").click()

    def tearDown(self):
        print('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
