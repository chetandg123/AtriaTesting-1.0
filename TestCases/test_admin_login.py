import time
from utilities import ExcelUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from PageObjects.AdminLoginPage import AdminLogin


class Test_Admin_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()

    def test_admin_login_page(self, setup):
        self.logger.info("******Testing admin login started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Atria WindPower":
            assert True
            self.driver.close()
            self.logger.info("******Testing admin login completed******")
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_login_title.png")
            self.driver.close()
            self.logger.info("******Testing admin login failed******")
            assert False


    def test_admin_login_with_valid_username_and_valid_password(self,setup):
        self.logger.info("******Testing admin login with valid username and password started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.admin_login = AdminLogin(self.driver)
        self.admin_login.setUserName(ReadConfig.getUsername())
        self.admin_login.setPassword(ReadConfig.getPassword())
        self.admin_login.clickLogin()
        if self.admin_login.getUserListTitile() == "Users List":
            assert True
            self.logger.info(
                "******Testing admin login with valid username and password successfully completed******")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******Testing admin login with valid username and password failed******")
            self.driver.close()
            assert False

    def test_admin_login_add_user_page(self,setup):
        self.logger.info("******Testing admin login user page exist or not started******")
        self.driver =setup
        al = AdminLogin(self.driver)
        al.adminLogin()
        al.clickAuthentication()
        al.clickAddUser()
        if al.getAddUserTitle() == "ADD USER":
            assert True
            self.logger.info("******Testing admin login user page exist or not completed******")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_userpage.png")
            self.logger.info("******Testing admin login user page exist or not failed******")
            self.driver.close()
            assert False

    def test_admin_login_add_user_without_entering_details(self,setup):
        self.logger.info("******Testing admin login add user without entering details started******")
        self.driver =setup
        al = AdminLogin(self.driver)
        al.adminLogin()
        al.clickAuthentication()
        al.clickAddUser()
        al.clickSubmit()
        if al.getAddUserUserNameErrorMsg() == "Username is required and should be unique" and al.getAddUserEmailErrorMsg() == "Email is required" and al.getAddUserPasswordErrorMsg() == "Password is required":
            assert True
            self.logger.info("******Testing admin login add user without entering details completed******")
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_addUser_without_entering_details.png")
            self.logger.info("******Testing admin login add user without entering details failed******")
            self.driver.close()
            assert False

    def test_admin_login_add_user_with_invalid_username_invalid_email_invalid_password(self,setup):
        self.starting_row_num = 2
        self.ending_row_num = 5
        self.logger.info("******Testing admin login add user with invalid username invalid email invalid passwprd "
                         "started******")
        self.driver =setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickAddUser()
        self.al.clickSubmit()
        status = []
        #Reading the data from excel file
        for r in range(self.starting_row_num, self.ending_row_num):
            self.add_user_username = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 1)
            self.add_user_email = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 4)
            self.add_user_password = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 5)
            self.add_user_exp = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 6)
            self.al.setAddUserUserName(self.add_user_username)
            self.al.setAddUserEmail(self.add_user_email)
            self.al.setAdduserSelectRole(self.add_user_role)
            self.al.setAdduserSelectAccessTo(self.add_user_accessTo)
            self.al.setAddUserPassword(self.add_user_password)
            self.al.clickSubmit()
            time.sleep(5)
            act_title = self.al.getAddUserSuccessMsg()
            exp_title = "User created successfully"

            if act_title == exp_title:
                if self.add_user_exp == "Pass":
                    self.al.clickLogin()
                    status.append("Pass")
                elif self.add_user_exp == "Fail":
                    self.al.clickLogin()
                    status.append("Fail")
            elif act_title != exp_title:
                if self.add_user_exp == "Pass":
                    status.append("Fail")
                elif self.add_user_exp == "Fail":
                    status.append("Pass")

        if "Fail" not in status:
            self.logger.info("******Testing admin login add user with invalid username invalid email invalid password "
                             "completed******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_addUser_by_entering_invalid_details.png")
            self.logger.info("******Testing admin login add user with invalid username invalid email invalid password "
                             "failed******")
            self.driver.close()
            assert False

    def test_admin_login_add_user_admin_ceo_manager(self, setup):
        self.starting_row_num = 5
        self.ending_row_num = 8
        self.logger.info("******Testing admin login add users(admin,ceo,manager) started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickAddUser()
        self.al.clickSubmit()
        status = []
        # Reading the data from excel file
        for r in range(self.starting_row_num, self.ending_row_num):
            self.add_user_username = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 1)
            self.add_user_email = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 4)
            self.add_user_password = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 5)
            self.add_user_exp = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 6)
            self.al.setAddUserUserName(self.add_user_username)
            self.al.setAddUserEmail(self.add_user_email)
            self.al.setAdduserSelectRole(self.add_user_role)
            self.al.setAdduserSelectAccessTo(self.add_user_accessTo)
            self.al.setAddUserPassword(self.add_user_password)
            self.al.clickSubmit()
            time.sleep(1)
            act_title = self.al.getAddUserSuccessMsg()
            exp_title = "User created successfully"
            if act_title == exp_title:
                if self.add_user_exp == "Pass":
                    status.append("Pass")
                elif self.add_user_exp == "Fail":
                    status.append("Fail")
            elif act_title != exp_title:
                if self.add_user_exp == "Pass":
                    status.append("Fail")
                elif self.add_user_exp == "Fail":
                    status.append("Pass")

        if "Fail" not in status:
            self.logger.info("******Testing admin login add users(admin,ceo,manager) completed******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_addUsers(admin,ceo,manger).png")
            self.logger.info("******Testing admin login add users(admin,ceo,manager) failed******")
            self.driver.close()
            assert False

    def test_admin_login_add_user_user_exist_error_msg(self, setup):
        self.starting_row_num = 5
        self.ending_row_num = 8
        self.logger.info("******Testing admin login user exist msg checking...******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickAddUser()
        self.al.clickSubmit()
        status = []
        # Reading the data from excel file
        for r in range(self.starting_row_num, self.ending_row_num):
            self.add_user_username = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 1)
            self.add_user_email = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 4)
            self.add_user_password = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 5)
            self.add_user_exp = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 6)
            self.al.setAddUserUserName(self.add_user_username)
            self.al.setAddUserEmail(self.add_user_email)
            self.al.setAdduserSelectRole(self.add_user_role)
            self.al.setAdduserSelectAccessTo(self.add_user_accessTo)
            self.al.setAddUserPassword(self.add_user_password)
            self.al.clickSubmit()
            time.sleep(2)

            act_title = self.al.getAddUserSuccessMsg()
            exp_title = "User exists with that name. Please create with different user"
            self.driver.refresh()
            if act_title == exp_title:
                if self.add_user_exp == "Pass":
                    status.append("Pass")
                elif self.add_user_exp == "Fail":
                    status.append("Fail")
            elif act_title != exp_title:
                if self.add_user_exp == "Pass":
                    status.append("Fail")
                elif self.add_user_exp == "Fail":
                    status.append("Pass")

        if "Fail" not in status:
            self.logger.info("******Testing admin login user exist msg checking completed...******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Testing admin login user exist msg checking failed...******")
            self.driver.close()
            assert False

    def test_admin_login_userlist_page(self,setup):
        self.logger.info("******Testing admin login user list displayed or not started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickUserList()
        if self.al.getUserListTitile() == "Users List":
            self.driver.close()
            assert True
            self.logger.info("******Testing admin login user list displayed successfully******")
        else:
            self.driver.save_screenshot("../Screenshots/"+"test_userlist_page.png")
            self.logger.info("******Testing admin login user list displayed or not failed******")
            self.driver.close()
            assert False

    def test_admin_login_userlist_created_users(self,setup):
        self.logger.info("******Testing admin login created users started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickUserList()
        time.sleep(2)
        res_list = []
        self.users_lst = self.al.getUsersList()
        for remove_id in self.users_lst:
            del remove_id[0]
        comp_list = self.al.getComparisionList()
        for x in comp_list:
            if x in self.users_lst:
                res_list.append(x)
        if res_list == comp_list:
            assert True,"Created users exist in the user list"
            self.logger.info("******Testing admin login created users completed******")
            self.driver.close()
        else :
            self.driver.save_screenshot("../Screenshots/" + "test_admin_login_created_users.png")
            self.logger.info("******Testing admin login created users failed******")
            self.driver.close()
            assert False,"Created users not exist in the user list"

    def test_admin_login_userlist_edit_option_for_all_users(self,setup):
        self.logger.info("******Testing admin login user list edit option checking started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        time.sleep(2)
        userlist = self.al.getUsersList()
        for ul in userlist:
            result = self.al.clickEditoption(ul[0])
            if result == "Users List":
                self.al.clickAddUserEditOptionCloseButton()
                assert True, "Edit option is working"
            else:
                self.driver.save_screenshot("../Screenshots/" + "test_admin_login_userlist_edit_option_failure.png")
                self.logger.info("******Testing admin login user list edit option checking failed******")
                self.driver.close()
                assert False, "Edit option is not working"
        self.driver.close()

    def test_admin_login_userlist_edit_users(self,setup):
        self.logger.info("******Testing admin login edit user's started******")
        self.starting_row_num = 8
        self.ending_row_num = 9
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickAddUser()
        # Reading the data from excel file
        for r in range(self.starting_row_num, self.ending_row_num):
            self.add_user_username = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 1)
            self.add_user_email = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 4)
            self.add_user_password = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 5)
            self.add_user_exp = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 6)
            self.al.setAddUserUserName(self.add_user_username)
            self.al.setAddUserEmail(self.add_user_email)
            self.al.setAdduserSelectRole(self.add_user_role)
            self.al.setAdduserSelectAccessTo(self.add_user_accessTo)
            self.al.setAddUserPassword(self.add_user_password)
            self.al.clickSubmit()
            time.sleep(2)
        self.driver.refresh()
        self.al.clickAuthentication()
        self.al.clickUserList()
        time.sleep(5)
        user_list = self.al.getUsersList()
        update_list = self.al.getExcelDeleteData(8, 9)
        row_num = []
        for x in update_list:
            for y in user_list:
                if y[1] == x:
                    row_num.append(y[0])
        excel_record= self.al.getExcelRecord(8,9)
        self.test_status = self.al.clickUpdateUser(row_num,excel_record)
        if "Fail" not in self.test_status:
            self.logger.info("******Testing admin login update user's successfully created******")
            self.driver.close()
            assert True,"Edit user successful for admin,ceo and manager"
        else:
            self.logger.info("******Testing admin login update user's failed******")
            self.driver.close()
            assert False,"Edit user Failed"

    def test_admin_login_userlist_edit_option_close_button(self,setup):
        self.logger.info("******Testing admin login adduser edit option started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAddUserEditOptionWithCloseButton(2)
        if self.al.getUserListTitile() == "Users List":
            self.logger.info("******Testing admin login adduser edit option completed******")
            assert True,"Close button working"
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_admin_login_edit_option.png")
            self.logger.info("******Testing admin login adduser edit option failed******")
            self.driver.close()
            assert False,"Close button is not working"

    def test_admin_login_userlist_delete(self, setup):
        self.delete_user_list = []
        self.starting_row_num = 9
        self.ending_row_num = 10
        self.logger.info("******Testing admin login adduser delete option started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        self.al.clickAuthentication()
        self.al.clickAddUser()
        # Getting the data from excel file and creating the new user in the atria add user page
        for r in range(self.starting_row_num, self.ending_row_num):
            self.add_user_username = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 1)
            self.delete_user_list.append(self.add_user_username)
            self.add_user_email = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 4)
            self.add_user_password = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 5)
            self.add_user_exp = ExcelUtils.readData(self.al.getExcelPath(), 'Add User', r, 6)
            self.al.setAddUserUserName(self.add_user_username)
            self.al.setAddUserEmail(self.add_user_email)
            self.al.setAdduserSelectRole(self.add_user_role)
            self.al.setAdduserSelectAccessTo(self.add_user_accessTo)
            self.al.setAddUserPassword(self.add_user_password)
            self.al.clickSubmit()
        time.sleep(2)
        self.al.clickAuthentication()
        self.al.clickUserList()
        time.sleep(2)
        user_list = self.al.getUsersList()
        delete_id = []
        for delete_user in self.delete_user_list:
            for user in user_list:
                if user[1] == delete_user:
                    delete_id.append(user[0])
        self.al.clickAddUserDeleteOption(delete_id)
        time.sleep(10)
        user_list_after_delete = self.al.getUsersList()
        get_deleted_user_list = self.delete_user_list
        self.status = False
        # Checking whether deleted user list still present in the userlist page
        for deleted_user in get_deleted_user_list:
            for user in user_list_after_delete:
                if user[1] == deleted_user:
                    self.status = True # if user found making status to true
        if self.status == False:
            self.logger.info("******Testing admin login adduser delete option completed******")
            assert True, "User deleted successfully"
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_admin_login_delete_option.png")
            self.logger.info("******Testing admin login adduser delete option failed******")
            self.driver.close()
            assert False, "User not deleted"

    def test_admin_login_logout(self,setup):
        self.logger.info("******Testing admin login logout started******")
        self.driver = setup
        self.al = AdminLogin(self.driver)
        self.al.adminLogin()
        time.sleep(3)
        self.al.clickLogout()
        if self.al.getLoginHeader() == "Login":
            self.logger.info("******Testing admin login logout completed******")
            assert True,"Logout is successful"
            self.driver.close()
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_admin_login_logout.png")
            self.logger.info("******Testing admin login logout failed******")
            self.driver.close()
            assert False,"Logout is unsuccessful"











