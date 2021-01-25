import time
class ManagerLogin:
    text_box_username_id="username"
    text_box_passsword_id="password"
    button_login_xpath="//*[@id='app']/div/div/div/div/div/button"
    turbines_G01_id='G01'
    turbines_G02_id = 'G02'
    turbines_G03_id = 'G03'
    turbines_G04_id = 'G04'
    turbines_G05_id = 'G05'
    turbines_G06_id = 'G06'
    turbines_G07_id = 'G07'
    turbines_G08_id = 'G08'
    turbines_G09_id = 'G09'
    turbines_G10_id = 'G10'
    turbines_G11_id = 'G11'
    turbines_G12_id = 'G12'
    turbines_G13_id = 'G13'
    turbines_G14_id = 'G14'
    turbines_G15_id = 'G15'
    list_turbine=['G01','G02','G03','G04','G05','G06','G07','G08','G09','G10','G11','G12','G13','G14','G15']
    back_button='backIcon'
    comment_xpath = '//*[@id="primary-content"]/div/div/div[1]/div[3]/span/div/div'
    comment_add_id='desc'
    comment_button_submit="saveComment"
    comment_header='/html/body/div[2]/div/div[1]/div/div/div/h5'
    comment_saved='/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/ul/li/div[2]'
    edit_button_id='//*[@id="editCommentBtn0"]'
    edit_input_id='//*[@id="editDesc0"]'
    update_button_xpath='//*[@id="updateComment0"]'
    updated_comment_xpath='/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/ul/li/div[2]'
    header_userlist_xpath = "//*[@id='primary-content']/div/div/div[1]/div[1]/h3"
    header_userloginerror_xpath="//*[@id='app']/div/div/div/div/div/p"
    select_windspeed_button_xpath = '//*[@id="main-menu"]/li'
    turbinG01_header_xpath='//*[@id="primary-content"]/div/div/div[1]/div[1]'
    delete_comment_id='deleteCommentBtn0'
    forecast_date_id='varianceasOnDate'
    start_date_id='variancestartDate'
    end_date_id='varianceendDate'
    windfarm_submit_button_id='submitBtn'
    windvariance_download_btn='varianceDownloadBtn'
    total_actual_power_id='actualPowerGen'
    total_forcast_power_id='forecastedPowerGen'


    forecast_45_day_id='forecastedasOnstartDate'
    windfrom_forecast_btn_id='forecastedSubmitBtn'
    wind_forecst_download_btn='forecastDownloadBtn'
    windform_45_forecast_id='forecastedPower'
    backbtn_id='backIcon'
    turbine_forecast_id='forecastPowerGen'

    gpalli_variance_csv ="gvpalli_variance.csv"
    gvpalli_forecasted_csv="gvpalli_forecasted"
    def __init__(self,driver):
        self.driver=driver



    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_box_passsword_id).clear()
        self.driver.find_element_by_id(self.text_box_passsword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def getuserdisplay(self):
        txt = self.driver.find_element_by_xpath(self.header_userlist_xpath).text
        return txt
    def getloginerror(self):
        err=self.driver.find_element_by_xpath(self.header_userloginerror_xpath).text
        return err
    def windTurbineclick(self):
        self.driver.find_element_by_xpath(self.select_windspeed_button_xpath).click()

    def getTurbines(self,list):
        self.driver.find_element_by_id(list).click()
        time.sleep(5)

    def getturbine_list(self):
        self.driver.find_element_by_xpath("//*[@id='main-menu']/li").click()
        lst = self.driver.find_elements_by_css_selector("ul.nav-submenu >li:nth-of-type(n)")
        turbine = []
        for i in lst:
            turbine.append(i.text)
        return  turbine








    def commentclick(self):
        self.driver.find_element_by_xpath(self.comment_xpath).click()
        time.sleep(5)

    def comment_add(self,comment_add):
        self.driver.find_element_by_id(self.comment_add_id).clear()
        self.driver.find_element_by_id(self.comment_add_id).send_keys(comment_add)


    def submit_button(self):
        self.driver.find_element_by_id(self.comment_button_submit).click()
        time.sleep((5))

    def comment_window_check(self):
        txt=self.driver.find_element_by_tag_name("h5").text
        return txt

    def comment_message(self):
        txt=self.driver.find_element_by_xpath(self.comment_saved).text
        return txt
    def comment_edit_button(self):
        self.driver.find_element_by_xpath(self.edit_button_id).click()
        time.sleep(5)
    def comment_edit_input(self,edit_comment):
        self.driver.find_element_by_xpath(self.edit_input_id).clear()
        self.driver.find_element_by_xpath(self.edit_input_id).send_keys(edit_comment)

    def update_comment(self):
        self.driver.find_element_by_xpath(self.update_button_xpath).click()
        time.sleep(5)

    def updated_check(self):
        txt = self.driver.find_element_by_xpath(self.updated_comment_xpath).text
        return txt

    def delete_comment_ok(self):
        self.driver.find_element_by_id(self.delete_comment_id).click()
        time.sleep(5)
        self.driver.switch_to_alert().accept()
        time.sleep(5)

    def delete_comment_cancel(self):
        self.driver.find_element_by_id(self.delete_comment_id).click()
        time.sleep(5)
        self.driver.switch_to_alert().dismiss()

    def forecast_date(self,forecast_variance_date):
        self.driver.find_element_by_id(self.forecast_date_id).clear()
        self.driver.find_element_by_id(self.forecast_date_id).send_keys(forecast_variance_date)
        time.sleep(3)

    def windvariance_chart_submit(self):
        self.driver.find_element_by_id(self.windfarm_submit_button_id).click()

    def windvariance_download(self):
        self.driver.find_element_by_id(self.windvariance_download_btn).click()
        time.sleep(5)
    def total_actual_power_find(self):
        txt=self.driver.find_element_by_id(self.total_actual_power_id).text
        return txt
    def total_forecast_power_find(self):
        txt=self.driver.find_element_by_id(self.total_forcast_power_id).text
        return txt

    def windform_forecast_date(self,forecast_date):
        self.driver.find_element_by_id(self.forecast_45_day_id).send_keys(forecast_date)

    def windform_forecast_button(self):
        self.driver.find_element_by_id(self.windfrom_forecast_btn_id).click()

    def wind_forecst_download(self):
        self.driver.find_element_by_id(self.wind_forecst_download_btn).click()
        time.sleep(5)

    def windform_future_45_forecast(self):
        txt=self.driver.find_element_by_id(self.windform_45_forecast_id).text
        return txt

    def turbine_page(self):
        txt = self.driver.find_element_by_tag_name("h5").text
        return txt

    def getbackbtn(self):
        self.driver.find_element_by_id(self.backbtn_id).click()

    def total_forecast_list_power_find(self):
        txt=self.driver.find_element_by_id(self.turbine_forecast_id).text
        return txt

