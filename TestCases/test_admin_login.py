from selenium import webdriver
from utilities.readProperties import ReadConfig
from PageObjects.AdminLoginPage import AdminLogin
from utilities.customLogger import LogGen
class Test_Admin_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()

    def test_admin_login_page(self, setup):
        self.logger.info("********************Test Admin Login Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Atria WindPower":
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_login_title.png")
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended Due to difference in the title********************************")
            assert False
    #
    # def test_admin_login_with_valid_username_and_valid_password(self,setup):
    #     self.logger.info("********************Test Admin Login With Valid Username And Password Started********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.admin_login = AdminLogin(self.driver)
    #     self.admin_login.setSelectUser("Admin")
    #     self.admin_login.setUserName(ReadConfig.getUsername())
    #     self.admin_login.setPassword(ReadConfig.getPassword())
    #      self.admin_login.clickLogin()
    #     if self.admin_login.getUserListPage() == "Users List":
    #         assert True
    #         self.logger.info(
    #             "********************Test Admin Login With Valid Username And Password successfully login********************************")
    #     else:
    #         self.driver.save_screenshot("../Screenshots/"+"test_admin_login_with_valid_username_and_valid_password.png")
    #         self.logger.info(
    #             "********************Test Admin Login With Valid Username And Password Failed********************************")
    #         self.driver.close()
    #         assert False






