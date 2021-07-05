# import pytest
# from selenium import webdriver
# from configuration.config import TestData
#
#
# @pytest.fixture(params=["chrome"], scope="class")
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     elif request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
#     # noinspection PyUnboundLocalVariable
#     web_driver.maximize_window()
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(10)
#     yield
#     web_driver.close()