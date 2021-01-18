import time

from PageObjects.AdminLoginPage import AdminLogin
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Atria_CEO_Screen:

    baseURL = ReadConfig.getApplicationURL()
    invalid_uname = ReadConfig.get_invalid_Username()
    invalid_pwd = ReadConfig.get_invalid_Password()
    logger = LogGen.logen()

    def test_login_as_ceo_user(self, setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.setUserName(ReadConfig.get_ceo_Username())
        self.login_page.setPassword(ReadConfig.get_ceo_Password())
        self.login_page.clickLogin()
        time.sleep(5)
        actual_content = self.driver.current_url
        if 'dashboard' in actual_content:
            print('CEO Page is displayed')
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Admin Page Ended Due to error msg is mismatch ********************************")
            assert False
