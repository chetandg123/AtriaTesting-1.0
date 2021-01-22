import csv
import os
import re
import time


from PageObjects.CEO_Page import ceo_page
from utilities.ExcelUtils import reuseable
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Atria_CEO_Turbines_Screen:

    baseURL = ReadConfig.getApplicationURL()
    invalid_uname = ReadConfig.get_invalid_Username()
    invalid_pwd = ReadConfig.get_invalid_Password()
    logger = LogGen.ceo_logs()
    #Dashboard Test Scripts

    def test_variance_chart_for_all_turbines(self ,setup):
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
        for i in range(2, 16):
            self.driver.find_element_by_xpath("//tbody/tr[{0}]".format(i)).click()
            time.sleep(4)
            print(self.driver.current_url,"is displayed")
            self.driver.find_element_by_id(self.login_page.varianceDownloadBtn).click()
            time.sleep(4)
            self.filename = self.files.get_download_dir() + '/' + self.login_page.list_turbine[i]+'_variance.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(self.login_page.list_turbine[i],' csv file is not download')
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
                    actual = (self.driver.find_element_by_id(self.login_page.actualPowerGen).text).replace('KWh', '')
                    forcast = (self.driver.find_element_by_id(self.login_page.forecastPowerGen).text).replace('KWh',
                                                                                                                '')
                    generated = float(re.sub('\f', "", actual).strip())
                    forcasting = float(re.sub('\f', "", forcast).strip())

                    act_generation = round(act_generation,2)
                    forcasted=round(forcasted,2)

                    print(act_generation,generated , forcasted,forcasting)

                    if act_generation != generated:
                        print('Difference found at actual generation ', act_generation, generated)
                        self.driver.save_screenshot("../Screenshots/" + "test_turbines_actgen_variance.png")
                        assert False
                    if forcasted != forcasting:
                        print('Difference found at actual forcasted ', forcasted, forcasting)
                        self.driver.save_screenshot("../Screenshots/" + "test_turbines_forcast_variance.png")
                        assert False
                    os.remove(self.filename)
                self.driver.find_element_by_id("backIcon").click()
            time.sleep(5)
        self.driver.close()

    def test_forcasted_chart_for_all_turbines(self, setup):
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
        for i in range(2, 16):
            self.driver.find_element_by_xpath("//tbody/tr[{0}]".format(i)).click()
            time.sleep(6)
            print(self.driver.current_url, "is displayed")
            self.driver.find_element_by_id(self.login_page.forecastDownloadBtn).click()
            time.sleep(4)
            self.filename = self.files.get_download_dir() + '/' + self.login_page.list_turbine[i]+'_forecasted.csv'
            if os.path.isfile(self.filename) != True:
                print(self.filename,self.login_page.list_turbine[i], ' csv file is not download')
                self.driver.close()
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    forcasted = 0
                    for row in csv.reader(fin):
                        print('\n', row)
                        forcasted += float(row[1])

                    ui_forcast = (self.driver.find_element_by_id(self.login_page.forecastedPower).text).replace('KWh',
                                                                                                              '')
                    ui_forcast = float(re.sub('\f', "", ui_forcast).strip())

                    forcasted = round(forcasted, 2)

                    print('file value',forcasted,'ui value', ui_forcast)

                    if forcasted != ui_forcast:
                        print('Difference found at actual generation ',forcasted,ui_forcast)
                        self.driver.save_screenshot("../Screenshots/" + "test_turbines_actgen_variance.png")
                        assert False

                    os.remove(self.filename)
                self.driver.find_element_by_id(self.login_page.backIcon).click()
            time.sleep(5)
        self.driver.close()