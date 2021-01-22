import time
from utilities import ExcelUtils
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from utilities.readProperties import ReadConfig
class AdminLogin:
    path = "../TestData/TestData.xlsx"
    text_box_username_id = "username"
    text_box_passsword_id = "password"
    button_login_xpath = "//*[@id='app']/div/div/div/div/div/button"
    button_logout_id = "logout"
    header_login_page_xpath ="//*[@id='app']/div/div/div/div/div/h3"
    # Admin AddUser Locators
    header_adduser_xpath = "//*[@id='primary-content']/div/div[1]/div/div/h3"
    text_box_adduser_username_id = "username"
    text_box_adduser_password_id = "password"
    text_box_adduser_email_id = "email"
    selectbox_adduser_role_id = "role"
    selectbox_adduser_accessto_id = "accessTo"
    button_submit_id="registerBtn"
    success_msg_css_selector = "div.card-body >p.text-center"
    # Admin AddUser Error messages Locators

    username_error_msg_id = "invalidUsername"
    email_error_msg_id = "invalidEmail"
    password_error_msg_id = "invalidPassword"

    #Admin UserList Locators

    header_userlist_xpath = "//*[@id='primary-content']/div/div[1]/div/div/h3"
    nav_authentication_css_selector = "ul#main-menu >li>a"
    nav_add_user_css_selector = "ul.nav-submenu > li >a"
    nav_userlist_css_selector = "ul.nav-submenu>li:last-of-type"
    editUser_id = "editUser"
    deleteUser_id = "deleteUser"
    failure_msg_css_selector = "div.card-body >p.text-center"
    update_user_close_button_xpath = "/html/body/div[4]/div/div/div[1]/button"

    text_box_updateuser_username_id = "username"
    text_box_updateuser_password_id = "password"
    text_box_updateuser_email_id = "email"
    selectbox_updateuser_role_id = "role"
    selectbox_updateuser_accessto_id = "accessTo"
    button_updateuser_submit_id = "updateBtn"

    def __init__(self,driver):
        self.driver=driver

    def getExcelPath(self):
        return self.path

    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_box_passsword_id).clear()
        self.driver.find_element_by_id(self.text_box_passsword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logout_id).click()

    def getLoginHeader(self):
        return self.driver.find_element_by_xpath(self.header_login_page_xpath).text

    def adminLogin(self):
        self.driver.get(ReadConfig.getApplicationURL())
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(ReadConfig.getUsername())
        self.driver.find_element_by_id(self.text_box_passsword_id).clear()
        self.driver.find_element_by_id(self.text_box_passsword_id).send_keys(ReadConfig.getPassword())
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    #Admin UserList Methods
    def getUserListTitile(self):
        txt = self.driver.find_element_by_xpath(self.header_userlist_xpath).text
        return txt

    def clickAuthentication(self):
        self.driver.find_element_by_css_selector(self.nav_authentication_css_selector).click()

    def clickAddUser(self):
        self.driver.find_element_by_css_selector(self.nav_add_user_css_selector).click()

    def clickUserList(self):
        self.driver.find_element_by_css_selector(self.nav_userlist_css_selector).click()

    def get_row_count(self):
        return len(self.driver.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.driver.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return self.get_row_count(),self.get_column_count()

    def row_data(self, row_number):
        row_number = row_number + 1
        row = self.driver.find_elements_by_xpath("//tr[" + str(row_number) + "]/td")
        rData = []
        for webElement in row:
            rData.append(webElement.text)
        return rData

    def getUserList(self):
        self.rows = AdminLogin.get_row_count(self)
        self.lst = []
        for x in range(0,self.rows):
            lst = AdminLogin.row_data(self,x)
            del lst[0]
            del lst[len(lst)-1]
            lst.append(lst)
        return self.lst

    def getComparisionList(self):
         return [['TestAdmin','admin','user_create'],['TestCeo','ceo','all'],['TestManager', 'manager', 'gvpalli']]

    def getUsersList(self):
        rows = len(self.driver.find_elements_by_tag_name("tr")) - 1
        created_users_lst = []
        i =1
        for x in range(0, rows):
            lst = AdminLogin.row_data(self,x)
            lst[0] = i
            i = i+1
            del lst[len(lst) - 1]
            created_users_lst.append(lst)
        return created_users_lst

    def getExcelDeleteData(self,rows,columns):
        excel_data=[]
        for r in range(rows, columns):
            self.add_user_username = ExcelUtils.readData(self.path, 'Add User', r, 1)
            excel_data.append(self.add_user_username)
        return excel_data

    def getExcelRecord(self,rows,columns):
        excel_data = []
        for r in range(rows, columns):
            self.add_user_username = ExcelUtils.readData(self.path, 'Add User', r, 1)
            self.add_user_email = ExcelUtils.readData(self.path, 'Add User', r, 2)
            self.add_user_role = ExcelUtils.readData(self.path, 'Add User', r, 3)
            self.add_user_accessTo = ExcelUtils.readData(self.path, 'Add User', r, 4)
            excel_data.append(self.add_user_username)
            excel_data.append(self.add_user_email)
            excel_data.append(self.add_user_role)
            excel_data.append(self.add_user_accessTo)
        return excel_data


    def getDeleteMessage(self):
        return self.driver.find_element_by_css_selector(self.failure_msg_css_selector).text


    def clickAddUserEditOption(self,rows):
        for x in range(1,rows):
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(x)).click()
            time.sleep(2)

    def clickUpdateUser(self,rows,update_list):
        self.test_status =[]
        self.update_values = []
        for x in rows:
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(x)).click()
            time.sleep(5)

            if AdminLogin.getUpdateUserUserName(self) == update_list[0] and AdminLogin.getUpdateUserEmail(self) == update_list[1] and AdminLogin.getUpdateUserSelectRole(self) == update_list[2] and AdminLogin.getUpdateUserSelectAccessTo(self) == update_list[3]:
                print("Auto Filling is working in the update user")
                self.update_values=["CheckAdmin","admin","user_create"]
                AdminLogin.setUpdateUserUserName(self,"CheckAdmin")
                AdminLogin.setUpdateUserEmail(self,"test@gmail.com")
                AdminLogin.setUpdateUserSelectRole(self,"Admin")
                AdminLogin.setUpdateUserSelectAccessTo(self,"User Create")
                AdminLogin.setUpdateUserPassword(self,"Test@1234")
                AdminLogin.clickUpdate(self)
                self.driver.refresh()
                user_list = AdminLogin.getUsersList(self)
                status = False
                for x in user_list:
                    del x[0]
                for y in user_list:
                    if y[0] == self.update_values[0] and y[1] == self.update_values[1] and y[2] == self.update_values[2]:
                        status = True
                if status == True:
                    self.test_status.append("Pass")
                    print("User is updated successfully for admin")
                else :
                    self.test_status.append("Fail")
            else:
                self.test_status.append("Fail")

        user_list = AdminLogin.getUsersList(self)
        row_num = []
        for x in self.update_values:
            for y in user_list:
                if y[1] == x:
                    row_num.append(y[0])
                    break
            break

        self.update_values1 = []
        for x in row_num:
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(x)).click()
            time.sleep(5)
            if AdminLogin.getUpdateUserUserName(self) == "CheckAdmin" and AdminLogin.getUpdateUserEmail(self) == "test@gmail.com" and AdminLogin.getUpdateUserSelectRole(self) == "Admin" and AdminLogin.getUpdateUserSelectAccessTo(self) == "User Create":
                print("Auto Filling is working in the update user")
                self.update_values1=["CheckCeo","ceo","all"]
                AdminLogin.setUpdateUserUserName(self,"CheckCeo")
                AdminLogin.setUpdateUserEmail(self,"test@gmail.com")
                AdminLogin.setUpdateUserSelectRole(self,"CEO")
                AdminLogin.setUpdateUserSelectAccessTo(self,"All")
                AdminLogin.setUpdateUserPassword(self,"Test@1234")
                AdminLogin.clickUpdate(self)
                self.driver.refresh()
                rows, columns = AdminLogin.get_table_size(self)
                user_list = AdminLogin.getUsersList(self)
                status = False
                for x in user_list:
                    del x[0]
                for y in user_list:
                    if y[0] == self.update_values1[0] and y[1] == self.update_values1[1] and y[2] == self.update_values1[2]:
                        status = True
                if status == True:
                    self.test_status.append("Pass")
                else:
                    self.test_status.append("Fail")
            else:
                self.test_status.append("Fail")

        user_list = AdminLogin.getUsersList(self)
        row_num = []
        for x in self.update_values1:
            for y in user_list:
                if y[1] == x:
                    row_num.append(y[0])
                    break
            break

        for x in row_num:
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(x)).click()
            time.sleep(2)
            if AdminLogin.getUpdateUserUserName(self) == "CheckCeo" and AdminLogin.getUpdateUserEmail(
                    self) == "test@gmail.com" and AdminLogin.getUpdateUserSelectRole(
                    self) == "CEO" and AdminLogin.getUpdateUserSelectAccessTo(self) == "All":
                print("Auto Filling is working in the update user")
                self.update_values2 = ["CheckManager", "manager", "gvpalli"]
                AdminLogin.setUpdateUserUserName(self, "CheckManager")
                AdminLogin.setUpdateUserEmail(self, "test@gmail.com")
                AdminLogin.setUpdateUserSelectRole(self, "Manager")
                AdminLogin.setUpdateUserSelectAccessTo(self, "GV Palli")
                AdminLogin.setUpdateUserPassword(self, "Test@1234")
                AdminLogin.clickUpdate(self)
                self.driver.refresh()
                user_list = AdminLogin.getUsersList(self)
                status = False
                for x in user_list:
                    del x[0]
                for y in user_list:
                    if y[0] == self.update_values2[0] and y[1] == self.update_values2[1] and y[2] == self.update_values2[2]:
                        status = True
                if status == True:
                    print("User is updated successfully for manager")
                    self.test_status.append("Pass")
                else:
                    self.test_status.append("Fail")
            else:
                self.test_status.append("Fail")

        return self.test_status


    def clickAddUserEditOptionWithCloseButton(self,rows):
        for x in range(1,rows):
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(x)).click()
            time.sleep(2)
            self.driver.find_element_by_css_selector("div.modal-header >button").click()
            time.sleep(2)

    def clickEditoption(self,row_num):
        self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[1]".format(row_num)).click()
        time.sleep(2)
        return AdminLogin.getUserListTitile(self)

    def clickAddUserEditOptionCloseButton(self):
        self.driver.find_element_by_css_selector("div.modal-header >button").click()
        time.sleep(5)

    def clickAddUserDeleteOption(self,rows):
        for x in rows:
            self.driver.find_element_by_xpath("//tr[{0}]/td[5]/span[2]".format(x)).click()
            time.sleep(2)



    #Admin AddUser Methods
    def getAddUserTitle(self):
        txt = self.driver.find_element_by_xpath(self.header_adduser_xpath).text
        return txt

    def setAddUserUserName(self,addUser_UserName):
        self.driver.find_element_by_id(self.text_box_adduser_username_id).clear()
        self.driver.find_element_by_id(self.text_box_adduser_username_id).send_keys(addUser_UserName)

    def setAddUserPassword(self,addUser_Password):
        self.driver.find_element_by_id(self.text_box_adduser_password_id).clear()
        self.driver.find_element_by_id(self.text_box_adduser_password_id).send_keys(addUser_Password)

    def setAddUserEmail(self,addUser_Email):
        self.driver.find_element_by_id(self.text_box_adduser_email_id).clear()
        self.driver.find_element_by_id(self.text_box_adduser_email_id).send_keys(addUser_Email)

    def setAdduserSelectRole(self,addUser_role):
        select = Select(self.driver.find_element_by_id(self.selectbox_adduser_role_id))
        select.select_by_visible_text(addUser_role)

    def setAdduserSelectAccessTo(self,addUser_accessTo):
        select = Select(self.driver.find_element_by_id(self.selectbox_adduser_accessto_id))
        select.select_by_visible_text(addUser_accessTo)

    def clickSubmit(self):
        self.driver.find_element_by_id(self.button_submit_id).click()

    def getAddUserUserNameErrorMsg(self):
        return self.driver.find_element_by_id(self.username_error_msg_id).text

    def getAddUserEmailErrorMsg(self):
        return self.driver.find_element_by_id(self.email_error_msg_id).text

    def getAddUserPasswordErrorMsg(self):
        return self.driver.find_element_by_id(self.password_error_msg_id).text

    def getAddUserSuccessMsg(self):
        return self.driver.find_element_by_css_selector(self.success_msg_css_selector).text

    def clickCloseButton(self):
        self.driver.find_element_by_xpath(self.update_user_close_button_xpath).click()

    def getUpdateUserUserName(self):
        input = self.driver.find_element_by_id("username")
        return input.get_attribute("value")

    def getUpdateUserPassword(self):
        input = self.driver.find_element_by_id(self.text_box_updateuser_password_id)
        return input.get_attribute("value")

    def getUpdateUserEmail(self):
        input = self.driver.find_element_by_id(self.text_box_updateuser_email_id)
        return input.get_attribute("value")

    def getUpdateUserSelectRole(self):
        select = Select(self.driver.find_element_by_id(self.selectbox_updateuser_role_id))
        value = select.first_selected_option
        return value.text

    def getUpdateUserSelectAccessTo(self):
        select = Select(self.driver.find_element_by_id(self.selectbox_updateuser_accessto_id))
        value = select.first_selected_option
        return value.text

    def setUpdateUserUserName(self,UpdateUserName):
        self.driver.find_element_by_id(self.text_box_updateuser_username_id).clear()
        self.driver.find_element_by_id(self.text_box_updateuser_username_id).send_keys(UpdateUserName)

    def setUpdateUserPassword(self,UpdatePassword):
        self.driver.find_element_by_id(self.text_box_updateuser_password_id).clear()
        self.driver.find_element_by_id(self.text_box_updateuser_password_id).send_keys(UpdatePassword)

    def setUpdateUserEmail(self,UpdateEmail):
        self.driver.find_element_by_id(self.text_box_updateuser_email_id).clear()
        self.driver.find_element_by_id(self.text_box_updateuser_email_id).send_keys(UpdateEmail)

    def setUpdateUserSelectRole(self,Role):
        select = Select(self.driver.find_element_by_id(self.selectbox_updateuser_role_id))
        select.select_by_visible_text(Role)

    def setUpdateUserSelectAccessTo(self,AccessTo):
        select = Select(self.driver.find_element_by_id(self.selectbox_updateuser_accessto_id))
        select.select_by_visible_text(AccessTo)

    def clickUpdate(self):
        self.driver.find_element_by_id(self.button_updateuser_submit_id).click()
