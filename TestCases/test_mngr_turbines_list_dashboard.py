
from get_directory import DirectoryPath
from utilities.readProperties import ReadConfig
from utilities.mamnager_turbinesLogger import managerLogGen
from PageObjects.ManagerLoginPage import ManagerLogin
import os.path
import os
import pandas as pd
import time


class Test_Manager_dashboard:
    baseURL = ReadConfig.getApplicationURL()
    manager_username = ReadConfig.getmanager_username()
    manager_password = ReadConfig.getmanager_password()
    logger = managerLogGen.logen()

    def test_manager_dashboard(self, setup):
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

        else:
            self.driver.save_screenshot(
                "../Screenshots/" + "test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With Valid Username And Password Failed********************************")
            self.driver.close()
            assert False
        self.file = DirectoryPath()

        sample=self.manager_dashboard.getturbine_list()
        self.logger.info(sample)
        for i in sample:
            self.manager_dashboard.getTurbines(i)
            time.sleep(5)

            self.manager_dashboard.forecast_date(ReadConfig.get_forecast_date())
            self.manager_dashboard.windvariance_chart_submit()
            self.filename = self.file.get_download_dir() + '/' + self.manager_dashboard.list_turbine[i]+'_variance.csv'
            if os.path.isfile(self.filename):


                os.remove(self.filename)
            else:
                print('no file')
            self.manager_dashboard.windvariance_download()
            if os.path.isfile(self.filename):
                assert True
                self.logger.info(
                "**********************In manager {} dashboard Actual v/s Forecasted chart file downloaded succesfully*******************************".format(i))
            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "{}_actual_forecast_downloaded.png".format(i))
                self.logger.info(
                "*************************In manager {} dashboard Actual v/s Forecasted chart file downloaded is failed*************************************".format(i))
                assert False

            df = pd.read_csv(self.filename)
            df_actual = df['Actual Power (KWh)'].sum()
            df_actual = int(df_actual)
            df_actual = str(df_actual)
            print(df_actual)
            df_forecast = df['Forecasted Power (KWh)'].sum()
            df_forecast = int(df_forecast)
            df_forecast = str(df_forecast)
            print(df_forecast)
            actual_power = self.manager_dashboard.total_actual_power_find()
            actual_power = actual_power.split(".")
            print(actual_power)
            forecast_power = self.manager_dashboard.total_forecast_list_power_find()
            forecast_power = forecast_power.split(".")
            print(forecast_power)
            if df_actual == actual_power[0]:
                assert True
                self.logger.info(
                "*************************downloaded {} actual and UI actual power generation are matched successfully****************".format(i))
            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "{}_actualvsuiactual_downloaded.png".format(i))
                self.logger.info(
                "****************************downloaded  {} actual and UI actual power generation are not  matched ********************************".format(i))
                assert False
            self.filename = self.file.get_download_dir() + '/' + self.manager_dashboard.list_turbine[i]+'_forecasted.csv'
            if df_forecast == forecast_power[0]:
                assert True
                self.logger.info(
                "*************************downloaded {} forecast and UI forcast power generation are matched successfully****************".format(i))
            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "{}_forecast_vs_uiforecast_downloaded.png".format(i))
                self.logger.info(
                "****************************downloaded  {} forecast and UI forecast power generation are not  matched ********************************".format(i))
                assert False
            if os.path.isfile(self.filename):

                os.remove((self.filename))
            else:
                print('no file')

            self.manager_dashboard.windform_forecast_button()
            self.manager_dashboard.wind_forecst_download()
            self.file = DirectoryPath()
            if os.path.isfile(self.filename):
                assert True
                self.logger.info(
                "**********************In manager {} dashboard 45 forecast file downloaded succesfully*******************************".format(i))
            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "{}_forecast_45_downloaded.png".format(i))
                self.logger.info(
                "*************************In manager {} dashboard 45 forecast chart file downloaded is failed*************************************".format(i))
                assert False

            self.manager_dashboard.getbackbtn()
            if self.manager_dashboard.getuserdisplay() == "Gvpalli Wind Farm":
                assert True
                self.logger.info(
                "********************back to windform Page successfully********************************")
                self.logger.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


            else:
                self.driver.save_screenshot(
                "../Screenshots/" + "windform_page.png")
                self.logger.info(
                "******************** back to windform Page failed********************************")
                self.logger.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                assert False
