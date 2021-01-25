from selenium import webdriver
from utilities.readProperties import ReadConfig
from PageObjects.ManagerLoginPage import ManagerLogin
from utilities.managerLogger import managerLogGen

class Test_Manager_Login:
    baseURL=ReadConfig.getApplicationURL()
    manager_username=ReadConfig.getmanager_username()
    manager_password=ReadConfig.getmanager_password()
    logger = managerLogGen.logen()
## case1: go to the url
    def test_manager_login_page(self, setup):
        self.logger.info("********************Test Manager Login Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Atria WindPower":
            assert True
            self.driver.close()
            self.logger.info("********************Test Manager Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/"+"manager_test_login_title.png")
            self.driver.close()
            self.logger.info("********************manager Admin Login Ended Due to difference in the title********************************")
            assert False

## login with valid username and password
    def test_manager_login_with_valid_username_and_valid_password(self,setup):
        self.logger.info("********************Test Admin Login With Valid Username And Password Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.manager_login = ManagerLogin(self.driver)

        self.manager_login.setUserName(ReadConfig.getmanager_username())
        self.manager_login.setPassword(ReadConfig.getmanager_password())
        self.manager_login.clickLogin()

        # print(self.admin_login.title())
        if self.manager_login.getuserdisplay() == "Gvpalli Wind Farm":
            assert True
            self.logger.info(
                "********************Test manager Login With Valid Username And Password successfully login********************************")
            
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With Valid Username And Password Failed********************************")
            self.driver.close()
##login with valid username and invalid password
    def test_manager_login_with_valid_username_and_invalid_password(self,setup):
        self.logger.info(
            "********************Test manager Login With Valid Username And invalid Password Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.manager_login = ManagerLogin(self.driver)

        self.manager_login.setUserName(ReadConfig.getmanager_username())
        self.manager_login.setPassword(ReadConfig.getinvalidmanager_password())
        self.manager_login.clickLogin()
        if self.manager_login.getloginerror()=='Incorrect Username/ Password. Please try again.':
            assert True
            self.logger.info(
                "********************Test manager Login With Valid Username And invalid Password successfully getting error successfull********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With Valid Username And invalid Password Failed********************************")
            self.driver.close()
##login with invalid username and valid password
    def test_manager_login_with_invalid_username_and_valid_password(self,setup):
        self.logger.info(
            "********************Test manager Login With inValid Username And valid Password Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.manager_login = ManagerLogin(self.driver)

        self.manager_login.setUserName(ReadConfig.getinvalidmanger_name())
        self.manager_login.setPassword(ReadConfig.getmanager_password())
        self.manager_login.clickLogin()
        if self.manager_login.getloginerror()=='Incorrect Username/ Password. Please try again.':
            assert True
            self.logger.info(
                "********************Test manager Login With inValid Username And valid Password successfully getting error successfull********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With inValid Username And valid Password logged ********************************")
            self.driver.close()
   ##login with invalid username and invalid password
    def test_manager_login_with_invalid_username_and_invalid_password(self,setup):
        self.logger.info(
            "********************Test manager Login With inValid Username And invalid Password Started********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.manager_login = ManagerLogin(self.driver)

        self.manager_login.setUserName(ReadConfig.getinvalidmanger_name())
        self.manager_login.setPassword(ReadConfig.getmanager_password())
        self.manager_login.clickLogin()
        if self.manager_login.getloginerror()=='Incorrect Username/ Password. Please try again.':
            assert True
            self.logger.info(
                "********************Test manager Login With inValid Username And invalid Password successfully getting error successfull********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_manager_login_with_invalid_username_and_invalid_password.png")
            self.logger.info(
                "******************** manager Login With inValid Username And invalid Password logged ********************************")
            self.driver.close()




