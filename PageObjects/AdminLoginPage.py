from selenium import webdriver
from selenium.webdriver.support.ui import Select
class AdminLogin:
    selectbox_selectuser_id="userType"
    text_box_username_id="username"
    text_box_passsword_id="password"
    button_login_id="login"

    # Admin AddUser Locators

    #Admin UserList Locators

    header_userlist_xpath = "//*[@id='primary-content']/div/div[1]/div/div/h3"

    def __init__(self,driver):
        self.driver=driver

    def setSelectUser(self,select_username):
        select = Select(self.driver.find_element_by_id(self.selectbox_selectuser_id))
        select.select_by_visible_text(select_username)

    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_box_passsword_id).clear()
        self.driver.find_element_by_id(self.text_box_passsword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    #Admin UserList Methods
    def getUserListPage(self):
        txt = self.driver.find_element_by_xpath(self.header_userlist_xpath).text
        return txt


    #Admin AddUser Methods



