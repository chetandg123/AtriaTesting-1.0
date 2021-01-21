import time

from PageObjects.AdminLoginPage import AdminLogin
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Atria_Login_Page:
    baseURL = ReadConfig.getApplicationURL()
    invalid_uname = ReadConfig.get_invalid_Username()
    invalid_pwd = ReadConfig.get_invalid_Password()
    logger = LogGen.logen()


    #Positive test scripts for login page
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
            self.driver.save_screenshot("../Screenshots/" + "test_login_title.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Login Ended Due to difference in the title********************************")
            assert False

    def test_login_as_admin_user(self, setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.setUserName(ReadConfig.getUsername())
        self.login_page.setPassword(ReadConfig.getPassword())
        self.login_page.clickLogin()
        time.sleep(5)
        actual_page = self.driver.current_url
        if  'users' in actual_page:
            assert True
            self.logger.info("********************Test Admin Page Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Admin Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_login_as_manager_user(self, setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.setUserName(ReadConfig.get_manager_Username())
        self.login_page.setPassword(ReadConfig.get_manager_Password())
        self.login_page.clickLogin()
        time.sleep(5)
        actual_content = self.driver.find_element_by_class_name('page-heading').text
        if  'Wind Farms' in actual_content:
            assert True
            self.driver.close()
            self.logger.info("********************Test Manager login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Manager Page Ended Due to error msg is mismatch ********************************")
            assert False

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
            assert True
            self.driver.close()
            self.logger.info("********************Test CEO Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test CEO Page Ended Due to error msg is mismatch ********************************")
            assert False


    #Negative test scripts for login page

    def test_login_without_inputs(self,setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page =AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.clickLogin()
        errormsg = self.driver.find_element_by_tag_name('p').text
        if errormsg == 'Please Enter user name and password':
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Login Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_login_without_password(self, setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.set_invalid_UserName(ReadConfig.get_invalid_Username())
        self.login_page.clickLogin()
        errormsg = self.driver.find_element_by_tag_name('p').text
        if errormsg == 'Please Enter username/password':
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Login Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_login_without_username(self, setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.set_invalid_UserName(ReadConfig.get_invalid_Password())
        self.login_page.clickLogin()
        errormsg = self.driver.find_element_by_tag_name('p').text
        if errormsg == 'Please Enter username/password':
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Login Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_login_with_valid_username_and_invalid_pwd(self,setup):
        self.logger.info("********************Test Login Page Started********************************")
        self.driver = setup
        self.login_page = AdminLogin(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.setUserName(ReadConfig.getUsername())
        self.login_page.set_invalid_UserName(ReadConfig.get_invalid_Password())
        self.login_page.clickLogin()
        errormsg = self.driver.find_element_by_tag_name('p').text
        if errormsg == 'Please Enter username/password':
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test Login Page Ended Due to error msg is mismatch ********************************")
            assert False
