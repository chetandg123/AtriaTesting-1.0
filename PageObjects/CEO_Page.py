import csv
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from PageObjects.AdminLoginPage import AdminLogin
from utilities.ExcelUtils import reuseable
from utilities.readProperties import ReadConfig


class ceo_page:

    button_login_id="login"
    dashboard ="dashboard"
    startdate_id="startDate"
    enddate_id="endDate"
    submit_id ="submit"
    submitBtn="submitBtn"
    line_chart_id ="line"
    bar_chart_id="bar"
    download_btn="downloadBtn"

    varianceDownloadBtn="varianceDownloadBtn"
    turbinesDownloadBtn="turbinesDownloadBtn"
    forecastDownloadBtn="forecastDownloadBtn"

    windfarm_csv="windfarms_variance.csv"
    gvpalli_variance="gvpalli_variance.csv"
    actual_generation="totalActualGen"
    total_forcasted="totalForecastedGen"
    gvpalli_img ="gvpalli"
    home_icon ="dashboardIcon"
    forcasted_Date="varianceasOnDate"
    windfarms ="//a/div"
    gvpalli_button ="//li[@id='gvpalli']"
    forcasted_onDate="forecastedasOnstartDate"
    forecastedendDate="forecastedendDate"
    forecastedSubmitBtn="forecastedSubmitBtn"
    #Windfarm button
    dashboard_windfarm ="//li[2]/a"
    header_userlist_xpath = "//*[@id='primary-content']/div/div[1]/div/div/h3"
    backIcon="backIcon"
    comments="comments"
    com_box="desc"
    edit_box="editDesc0"
    sample_text="Sample Text"
    updated_text="QA Sample Text"
    saveComment="saveComment"
    updatedcomment="editCommentBtn0"
    update_btn="updateComment0"
    delete_comment="deleteCommentBtn0"
    #GVPalli
    actualPowerGen="actualPowerGen"
    forecastedPowerGen="forecastedPowerGen"
    gvpalli_forecasted="gvpalli_forecasted.csv"
    forecastedPower="forecastedPower"
    turbinesDownload="turbinesDownloadBtn"
    turbine_details="turbine_details.csv"
    turbine_forcasted ="turbine_forcasted.csv"
    # Turbines
    list_of_turbines="//tr"
    turbine_01="G01"
    turbine_02="G02"
    turbine_03="G03"
    turbine_04="G04"
    tur_actualPowerGen="actualPowerGen"
    tur_forecastPowerGen="forecastPowerGen"
    turbineHistoryDownloadBtn="turbineHistoryDownloadBtn"
    turbine_history ="turbine_history.csv"

    varianceendDate="varianceendDate"

    def __init__(self,driver):
        self.driver=driver

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    #Admin UserList Methods
    def getUserListPage(self):
        txt = self.driver.find_element_by_xpath(self.header_userlist_xpath).text
        return txt

    def get_ceo_screen(self):
        self.driver.maximize_window()
        self.login_page = AdminLogin(self.driver)
        self.login_page.setUserName(ReadConfig.get_ceo_Username())
        self.login_page.setPassword(ReadConfig.get_ceo_Password())
        self.login_page.clickLogin()
        time.sleep(5)

    def get_turbines_list(self):
        self.driver.find_element_by_xpath("//*[@id='main-menu']/li").click()
        lst = self.driver.find_elements_by_css_selector("ul.nav-submenu >li:nth-of-type(n)")
        turbine=[]
        for i in lst:
            turbine.append(i.text)
        return turbine

    def check_variance_chart(self):
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.find_element_by_id(self.login_page.forcasted_onDate).clear()
        time.sleep(2)
        startDate = self.driver.find_element_by_id(self.login_page.forcasted_onDate)
        startDate.send_keys('10/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.forecastedendDate)
        endDate.send_keys('20/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.varianceDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.gvpalli_variance
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm variance csv file is not download')
            self.driver.close()
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    print('\n', row)
                    act_generation += float(row[2])
                    forcasted += float(row[1])

                actual = (self.driver.find_element_by_id(self.login_page.tur_actualPowerGen).text).replace('KWh', '')
                forcast = (self.driver.find_element_by_id(self.login_page.tur_forecastPowerGen).text).replace('KWh', '')

                generated = float(re.sub('\f', "", actual).strip())
                forcasting = float(re.sub('\f', "", forcast).strip())

                generated = round(generated,2)
                forcasting =  round(forcasting,2)

                act_generation = round(act_generation,2)
                forcasted = round(forcasted,2)

                print(generated, ":", type(generated), act_generation, ":", type(act_generation), forcasting, ":",
                      type(forcasting), forcasted, ":", type(forcasted))

                if int(act_generation) != int(generated):
                    print('Difference found at actual generation ', act_generation, generated)
                if int(forcasted) != int(forcasting):
                    print('Difference found at actual forcasted ', forcasted, forcasting)
                os.remove(self.filename)
                self.driver.close()
            self.driver.close()

    def check_turbines_forcasted_chart(self):
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.find_element_by_id(self.login_page.forcasted_onDate).clear()
        time.sleep(2)
        startDate = self.driver.find_element_by_id(self.login_page.forcasted_onDate)
        startDate.send_keys('10/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.forecastedendDate)
        endDate.send_keys('20/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.varianceDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.turbine_02+"_variance.csv"
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm variance csv file is not download')
            self.driver.close()
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    print('\n', row)
                    act_generation += float(row[2])
                    forcasted += float(row[1])

                actual = (self.driver.find_element_by_id(self.login_page.actualPowerGen).text).replace('MWh', '')
                forcast = (self.driver.find_element_by_id(self.login_page.forecastedPowerGen).text).replace('MWh', '')

                generated = float(re.sub('\f', "", actual).strip())
                forcasting = float(re.sub('\f', "", forcast).strip())

                generated = round(generated, 2)
                forcasting = round(forcasting, 2)

                act_generation = round(act_generation, 2)
                forcasted = round(forcasted, 2)

                print(generated,":",type(generated),act_generation,":",type(act_generation),forcasting,":",type(forcasting),forcasted,":",type(forcasted))
                if int(act_generation) != int(generated):
                    print('Difference found at actual generation ', act_generation, generated)
                if int(forcasted) != int(forcasting):
                    print('Difference found at actual forcasted ', forcasted, forcasting)
                os.remove(self.filename)
