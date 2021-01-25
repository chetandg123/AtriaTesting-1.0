from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.manager_comment_section import managerLogGen
from PageObjects.ManagerLoginPage import ManagerLogin


class Test_Manager_comment_section:
    baseURL = ReadConfig.getApplicationURL()
    manager_username = ReadConfig.getmanager_username()
    manager_password = ReadConfig.getmanager_password()
    logger = managerLogGen.logen()
    def test_manager_dashboard(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.manager_dashboard = ManagerLogin(self.driver)
        self.manager_dashboard.setUserName(ReadConfig.getmanager_username())
        self.manager_dashboard.setPassword(ReadConfig.getmanager_password())
        self.manager_dashboard.clickLogin()
        if self.manager_dashboard.getuserdisplay() == "Gvpalli Wind Farm":
            assert True
            self.logger.info(
                "********************Test manager Login With Valid Username And Password successfully login********************************")
            self.manager_dashboard.commentclick()

            print(self.manager_dashboard.comment_window_check())
            if self.manager_dashboard.comment_window_check()=='Comments History':
                assert True
                self.logger.info("********comment window opened successfully********************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "comment_window_open.png")
                self.logger.info("*********************comment_window_opened_failed")

            self.manager_dashboard.comment_add(ReadConfig.getcomment_add())
            self.manager_dashboard.submit_button()
            if self.manager_dashboard.comment_message()=='Message : sample':
                assert True
                self.logger.info(
                    "********************commented succesfully********************************")
            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "comment_window.png")
                self.logger.info("*********************commenting is failed************")
            self.manager_dashboard.comment_edit_button()
            self.manager_dashboard.comment_edit_input(ReadConfig.getedit_input())
            self.manager_dashboard.update_comment()
            if self.manager_dashboard.updated_check()=='Message : sample updated':
                self.logger.info(
                    "********************comment updated succesfully********************************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "updated_comment.png")
                self.logger.info("********************* updated commenting is failed************")
            self.manager_dashboard.delete_comment_cancel()
            if self.manager_dashboard.updated_check() == 'Message : sample updated':
                self.logger.info(
                    "******************** deletion cancellation the comment is succesfully********************************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "delete_comment.png")
                self.logger.info("*********************deletion cancellation the comment is  failed************")

            self.manager_dashboard.delete_comment_ok()
            if self.manager_dashboard.updated_check()!='Message : sample updated':
                self.logger.info(
                    "******************** deleted the comment is succesfully********************************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "delete_comment.png")
                self.logger.info("********************* deleted the comment  is failed************")



        else:
            self.driver.save_screenshot(
                "../Screenshots/" + "test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With Valid Username And Password Failed********************************")
            self.driver.close()


