import csv
import os
import re
import time


from PageObjects.CEO_Page import ceo_page
from get_directory import reuseable
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Atria_CEO_Screen:

    baseURL = ReadConfig.getApplicationURL()
    invalid_uname = ReadConfig.get_invalid_Username()
    invalid_pwd = ReadConfig.get_invalid_Password()
    logger = LogGen.ceo_logs()
    #Dashboard Test Scripts

    def test_login_as_ceo_user(self, setup):
        self.logger.info("********************Test CEO Login Page Started********************************")
        self.driver = setup
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        actual_content = self.driver.current_url
        if  self.login_page.dashboard in actual_content:
            print('CEO Page is displayed')
            assert True
            self.driver.close()
            self.logger.info("********************Test CEO Login Ended********************************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login_page.png")
            self.driver.close()
            self.logger.info(
                "********************Test CEO Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_ceo_dashboard_button(self, setup):
        self.logger.info("********************Test  CEO Page Started********************************")
        self.driver = setup
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(3)
        actual_content = self.driver.current_url
        if  self.login_page.dashboard in actual_content:
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

    def test_forcast_dashboards(self, setup):
        self.logger.info("********************Test CEO Page Started********************************")
        self.driver = setup
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(3)
        actual_content = self.driver.current_url
        if  self.login_page.dashboard in actual_content:
            print('CEO Page is displayed')
            assert True
            self.driver.close()
            self.logger.info("********************Test Admin Login Ended********************************")
        else:
            self.driver.close()
            self.logger.info(
                "********************Test  forcasted dashboard Page Ended Due to error msg is mismatch ********************************")
            assert False



    def test_windfarms_icons(self,setup):
        self.logger.info("********************Test CEO Wind farms Page Started********************************")
        self.driver = setup
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(8)
        self.driver.find_element_by_id(self.login_page.gvpalli_img).click()
        time.sleep(3)
        actual_content = self.driver.current_url
        if self.login_page.gvpalli_img in actual_content:
            print('GV Palli wind farm is displayed')
            assert True
            self.driver.find_element_by_id(self.login_page.home_icon).click()
            time.sleep(3)
            self.driver.close()
            self.logger.info("********************Test GV Palli windfarm icon Ended********************************")
        else:
            self.driver.close()
            self.logger.info(
                "********************Test  forcasted dashboard Page Ended Due to error msg is mismatch ********************************")
            assert False

    def test_start_date_picker(self,setup):
        self.logger.info("********************Test Start Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.startdate_id).clear()
        time.sleep(2)
        startdt = self.driver.find_element_by_id(self.login_page.startdate_id)
        startdt.send_keys('17/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(5)
        self.driver.close()
        self.logger.info(
                    "********************Test Start date is  Ended Due to error msg is mismatch ********************************")

    def test_end_date_picker(self,setup):
        self.logger.info("********************Test end Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test end date is  Ended Due to error msg is mismatch ********************************")

    def test_check_download_icon(self, setup):
        self.logger.info("********************Test ceo download icon  Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.download_btn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.windfarm_csv
        if os.path.isfile(self.filename) != True:
            print('Windfarm variance csv file is not download')
            count = count + 1
            assert False
        os.remove(self.filename)
        self.driver.close()
        self.logger.info("********************Tested Downloading csv file is mismatch *********")

    def test_windfarms(self,setup):
        self.logger.info("********************Test ceo download icon  Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        windfarms = self.driver.find_elements_by_xpath(self.login_page.windfarms)
        images = len(windfarms)
        if images == 0 :
            assert False
        self.driver.close()
        self.logger.info("********************Tested Downloading csv file is mismatch *********")

    def test_forcasted_line_and_bar_charts(self, setup):
        self.logger.info("********************Test line and bar Graph Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.startdate_id).clear()
        time.sleep(2)
        startDate = self.driver.find_element_by_id(self.login_page.startdate_id)
        startDate.send_keys('17/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.line_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.bar_chart_id).click()
        time.sleep(2)
        self.driver.close()
        self.logger.info("************************Bar and Line chart testing ends***************** ")

    def test_forcasted_graph_and_downloadcsv(self, setup):
        self.logger.info("********************Test forcasted Graph Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.startdate_id).clear()
        time.sleep(2)
        startDate = self.driver.find_element_by_id(self.login_page.startdate_id)
        startDate.send_keys('20/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('22/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.line_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.bar_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.download_btn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.windfarm_csv
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm variance csv file is not download')
            count = count + 1
            self.driver.close()
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    print('\n',row)
                    act_generation += float(row[2])
                    forcasted += float(row[1])

                actual = (self.driver.find_element_by_id(self.login_page.actual_generation).text).replace('MWh','')
                forcast=(self.driver.find_element_by_id(self.login_page.total_forcasted).text).replace('MWh','')
                generated = float(re.sub('\f', "", actual).strip())
                forcasting =float(re.sub('\f' ,"",forcast).strip())
                if  act_generation != generated:
                    print('Difference found at actual generation ',act_generation ,generated)
                    count = count + 1
                    assert False
                if  forcasted != forcasting:
                    print('Difference found at actual forcasted ',forcasted , forcasting)
                    count = count + 1
                    assert False
                os.remove(self.filename)
            self.driver.close()
            self.logger.info("******************checked with wind farm variance ****************")


    # Wind Farm button

    def test_click_on_wind_farm_button(self, setup):
        self.logger.info("********************Test forcasted Graph Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        wf = self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).text
        if  wf != "Wind Farms":
            print('Wind form button is clicked ')
            assert False
        self.driver.close()
        self.logger.info("******************checked with wind farm button ****************")

    def test_click_on_wind_farm_options(self, setup):
        self.logger.info("********************Test forcasted Graph Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        header = self.driver.find_element_by_tag_name('h3').text
        if header == "Gvpalli Wind Farm":
            print('Gvpalli Wind Farm is displayed')
            assert True
        else:
            assert False
        self.driver.close()
        self.logger.info("******************checked with wind farm button ****************")

    # GV palli windfarm

    def test_click_on_gv_palli_wind_farm_options(self, setup):
        self.logger.info("********************Test forcasted Graph Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        header = self.driver.find_element_by_tag_name('h3').text
        if header == "Gvpalli Wind Farm":
            print('Gvpalli Wind Farm is displayed')
            assert True
        else:
            assert False
        self.driver.close()
        self.logger.info("******************checked with wind farm button ****************")

    def test_gvpalli_start_date_picker(self,setup):
        self.logger.info("********************Test Start Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.startdate_id).clear()
        time.sleep(2)
        startdt = self.driver.find_element_by_id(self.login_page.startdate_id)
        startdt.send_keys('17/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test Start date is  Ended Due to error msg is mismatch ********************************")

    def test_gvpalli_end_date_picker(self,setup):
        self.logger.info("********************Test end Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.dashboard).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.enddate_id).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.enddate_id)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submit_id).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test end date is  Ended Due to error msg is mismatch ********************************")

    def test_check_variance_csv_file_download_icon(self, setup):
        self.logger.info("********************Test ceo download icon  Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.varianceDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.gvpalli_variance
        if os.path.isfile(self.filename) != True:
            print('Windfarm variance csv file is not download')
            count = count + 1
            assert False
        os.remove(self.filename)
        self.driver.close()
        self.logger.info("********************Tested Downloading csv file is mismatch *********")


    def test_gvpalli_forcasted_line_and_bar_charts(self, setup):
        self.logger.info("********************Test line and bar Graph Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
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
        self.driver.find_element_by_id(self.login_page.line_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.bar_chart_id).click()
        time.sleep(2)
        self.driver.close()
        self.logger.info("************************Bar and Line chart testing ends***************** ")

    def test_gvpalli_variance_graph_and_downloadcsv(self, setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        count =0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
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
            count = count + 1
            self.driver.close()
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    print('\n',row)
                    act_generation += float(row[1])
                    forcasted += float(row[2])

                actual_ui = (self.driver.find_element_by_id(self.login_page.actualPowerGen).text).replace('MWh','')
                forcast_ui=(self.driver.find_element_by_id(self.login_page.forecastedPowerGen).text).replace('MWh','')

                generated = float(re.sub('\f', "", actual_ui).strip())
                forcasting =float(re.sub('\f' ,"",forcast_ui).strip())

                print(generated ,act_generation)
                os.remove(self.filename)
                if  act_generation != generated:
                    print('Difference found at actual generation ',act_generation ,generated)
                    count = count + 1
                    assert False
                if  forcasted != forcasting:
                    print('Difference found at actual forcasted ',forcasted , forcasting)
                    count = count + 1
                    assert False
            self.driver.close()
            self.logger.info("******************checked with wind farm variance ****************")

    def test_gvpalli_forcasted_download_icon(self, setup):
        self.logger.info("********************Test gv palli forcasted download icon Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.forcasted_onDate).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forecastDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.gvpalli_forecasted
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm forcasted csv file is not download')
        else:
            os.remove(self.filename)
        self.driver.close()
        self.logger.info('*********************checked forcasted download icon *****************')

    def test_gvpalli_forcasted_graph_and_downloadcsv(self, setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.forcasted_onDate).clear()
        time.sleep(2)
        # startDate = self.driver.find_element_by_id(self.login_page.forcasted_onDate)
        # startDate.send_keys('10/01/2021')
        # time.sleep(2)
        # self.driver.find_element_by_id(self.login_page.forecastedendDate).clear()
        # time.sleep(2)
        # endDate = self.driver.find_element_by_id(self.login_page.forecastedendDate)
        # endDate.send_keys('20/01/2021')
        # time.sleep(2)
        # self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        # time.sleep(3)
        self.driver.find_element_by_id(self.login_page.line_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.bar_chart_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.gvpalli_forecasted
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm forcasted csv file is not download')
            self.driver.close()
        else:

            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    forcasted += float(row[1])

                forcast=(self.driver.find_element_by_id(self.login_page.forecastedPower).text).replace('MWh','')
                forcasting =float(re.sub('\f' ,"",forcast).strip())
                print(forcast,forcasting)
                if  forcasted != forcasting:
                    print('Difference found at actual generation ',forcasting , forcasted)
                    assert False
                os.remove(self.filename)
            self.driver.close()
            self.logger.info("******************checked with wind farm variance ****************")

    # Comments
    def test_clicking_on_comment_icon_box(self,setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.comments).click()
        comment_box = self.driver.find_element_by_tag_name('h5').text
        if comment_box == 'Comments History':
            print('Comment box is displayed')
            self.driver.close()
        else:
            self.driver.close()
        self.logger.info("****************Checked with comment icon *****************")

    def test_adding_comment_in_box(self, setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.comments).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.com_box).send_keys(self.login_page.sample_text)
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.saveComment).click()
        time.sleep(3)
        if self.login_page.sample_text in self.driver.page_source:
            print('Comment is updated and displayed')
            assert True
            self.driver.close()

        else:
            assert False
        self.logger.info("****************Checked with comment icon *****************")

    def test_update_existing_comment_in_box(self, setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.comments).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.updatedcomment).click()
        self.driver.find_element_by_id(self.login_page.edit_box).send_keys(self.login_page.updated_text)
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.update_btn).click()
        time.sleep(3)
        if self.login_page.updated_text in self.driver.page_source:
            print('Comment is updated and displayed')
            assert True
            self.driver.close()

        else:
            assert False
        self.logger.info("****************Checked with comment icon *****************")

    def test_delete_comment_in_box(self, setup):
        self.logger.info("********************Test gv palli forcasted Graph Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.comments).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.delete_comment).click()
        alertobj = self.driver.switch_to_alert()
        alertobj.accept()
        time.sleep(2)
        if self.login_page.updated_text not in self.driver.page_source:
            assert True
            self.driver.close()
        self.logger.info("****************Checked deleted comment from comment box *****************")


    # GV Palli Turbines

    def test_check_turbine_list_table_contains_turbines_and_downlaod_csv(self,setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        turbines = self.driver.find_elements_by_xpath(self.login_page.list_of_turbines)
        count = len(turbines) - 1
        if count == 15:
            print('Turbines links are present')
        else:
            print('Turbines links are not present')
        turbine_file = self.driver.find_element_by_id(self.login_page.turbinesDownload).click()
        time.sleep(4)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.turbine_details
        if os.path.isfile(self.filename) != True:
            print('Windfarm forcasted csv file is not download')
            self.driver.close()
        else:
            with open(self.filename) as fin:
                reader = csv.reader(fin, delimiter=",")
                data = list(reader)
                row_count = len(data)
                if row_count != 0 :
                    assert True
            os.remove(self.filename)
            self.driver.close()
        self.logger.info("***************************Turbines csv file and list of turbines*****************")

    def test_g02_tubine_details_varicance_chart(self, setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        turbine_name = self.login_page.turbine_02
        if turbine_name in self.driver.find_element_by_tag_name('h5').text:
            assert True
            print(turbine_name ,"is displayed ")
        else:
            assert False
        self.login_page.check_variance_chart()
        self.logger.info("***************************Turbines csv file and list of turbines*****************")

    def test_g02_tubine_forcasted_chart(self, setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        turbine_name = self.login_page.turbine_02
        if turbine_name not in self.driver.find_element_by_tag_name('h5').text:
            assert False
        else:
            self.login_page.check_turbines_forcasted_chart()
            self.driver.close()
            self.logger.info("***************************Turbines csv file and list of turbines*****************")

    def test_download_icon_for_forcasted(self,setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forecastDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.turbine_forcasted
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm forcasted csv file is not download')
        else:
            os.remove(self.filename)
        self.driver.close()
        self.logger.info("*******************Downloading forcasted csv file of turbine****************")

    def test_check_total_power_forcasted_values(self,setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forecastDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.turbine_forcasted
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Windfarm forcasted csv file is not download')
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                act_generation = 0
                forcasted = 0
                for row in csv.reader(fin):
                    forcasted += float(row[1])

                forcast = (self.driver.find_element_by_id(self.login_page.forecastedPower).text).replace('/MWh', '')
                forcasting = float(re.sub('\f', "", forcast).strip())
                print(forcast, forcasting)
                if forcasted != forcasting:
                    print('Difference found at actual generation ', forcasting, forcasted)
                    assert False
            os.remove(self.filename)
        self.driver.close()
        self.logger.info("*******************Downloading forcasted csv file of turbine****************")

    def test_log_history_download_icon(self,setup):
        self.logger.info("********************Test gv palli Turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.turbineHistoryDownloadBtn).click()
        time.sleep(3)
        self.filename = self.files.get_download_dir() + '/' + self.login_page.turbine_history
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Turbine history csv file is not download')
        else:
            os.remove(self.filename)
        self.driver.close()
        self.logger.info("*******************Downloading forcasted csv file of turbine**************")

    def test_start_date_picker_for_variance_turbine(self,setup):
        self.logger.info("********************Test Start Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forcasted_Date).clear()
        time.sleep(2)
        startdt = self.driver.find_element_by_id(self.login_page.forcasted_Date)
        startdt.send_keys('17/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.varianceendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.varianceendDate)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submitBtn).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test Start date is  Ended Due to error msg is mismatch ********************************")

    def test_end_date_picker_for_variance_turbine(self,setup):
        self.logger.info("********************Test end Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.varianceendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.varianceendDate)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.submitBtn).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test end date is  Ended Due to error msg is mismatch ********************************")

    def test_start_date_picker_for_forcasted_turbine(self,setup):
        self.logger.info("********************Test Start Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forcasted_onDate).clear()
        time.sleep(2)
        startdt = self.driver.find_element_by_id(self.login_page.forcasted_onDate)
        startdt.send_keys('17/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.forecastedendDate)
        endDate.send_keys('19/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test Start date is  Ended Due to error msg is mismatch ********************************")

    def test_end_date_picker_for_forcasted_turbine(self,setup):
        self.logger.info("********************Test end Date picker Started********************************")
        self.driver = setup
        count = 0
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.login_page.turbine_02).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.login_page.forecastedendDate).clear()
        time.sleep(2)
        endDate = self.driver.find_element_by_id(self.login_page.forecastedendDate)
        endDate.send_keys('21/01/2021')
        time.sleep(2)
        self.driver.find_element_by_id(self.login_page.forecastedSubmitBtn).click()
        time.sleep(3)
        self.driver.close()
        self.logger.info(
                    "********************Test end date is  Ended Due to error msg is mismatch ********************************")

    def test_click_on_each_turbines(self, setup):
        self.logger.info("********************Test all turbines Started********************************")
        self.driver = setup
        self.files = reuseable()
        self.driver.implicitly_wait(200)
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(8)
        lst = len(self.driver.find_elements_by_tag_name("tr")) - 1
        for i in range(1, 16):
            self.driver.find_element_by_xpath("//tbody/tr[{0}]".format(i)).click()
            time.sleep(4)
            print(self.driver.current_url, "is displayed")
            self.driver.find_element_by_id("backIcon").click()
            time.sleep(5)
        self.driver.close()

























