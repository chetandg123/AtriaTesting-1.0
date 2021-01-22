import time

from PageObjects.CEO_Page import ceo_page
from utilities.ExcelUtils import reuseable
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_turbines_of_each_windfarms():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.ceo_logs()


    def test_gvpalli_forcasted_graph_and_downloadcsv(self, setup):
        self.logger.info("********************Test gv palli all turbines Started********************************")
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
        turbines = self.driver.find_elements_by_tag_name('tr')
        for i in range(1,len(turbines)):
            turbines[i].click()
            time.sleep(3)
            self.driver.find_element_by_id(self.login_page.backIcon).click()
            time.sleep(5)
        self.driver.close()
        self.logger.info('******************* GV Palli turbines completed*******************')

    def test_gvpalli_all_turbines_downloadcsv(self, setup):
        self.logger.info("********************Test gv palli all turbines Started********************************")
        self.driver = setup
        self.driver.implicitly_wait(100)
        self.files = reuseable()
        self.login_page = ceo_page(self.driver)
        self.driver.get(self.baseURL)
        self.login_page.get_ceo_screen()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.login_page.dashboard_windfarm).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.login_page.gvpalli_button).click()
        time.sleep(5)
        # turbines =self.driver.find_elements_by_xpath('//tr')
        # turbi =self.driver.find_elements_by_xpath('//li/a')
        # for i in range(1, len(turbines)):
        #     time.sleep(2)
        #     turbines[i].click()
        #     time.sleep(5)
        #     self.driver.find_element_by_xpath("//*[@id='main-menu']/li[2]/a").click()
        #     time.sleep(2)
        #     self.driver.implicitly_wait(30)
        #     for j in range(3,len(turbi)):
        #         turbi[j].click()
        #         time.sleep(10)

        turbines = self.driver.find_elements_by_id('G01').click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='main-menu']/li[2]/a").click()
        time.sleep(2)
        for i in range(1, 15):
            self.driver.find_element_by_id(('G0', i)).click()
        self.driver.close()
        self.logger.info('******************* GV Palli turbines completed*******************')
