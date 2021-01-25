from get_directory import DirectoryPath
from utilities.readProperties import ReadConfig
from utilities.mgnr_dash_Logger import managerLogGen
from PageObjects.ManagerLoginPage import ManagerLogin
import os.path
import os
import pandas as pd

class Test_Manager_dashboard:
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
        self.files = DirectoryPath()
        if self.manager_dashboard.getuserdisplay() == "Gvpalli Wind Farm":
            assert True
            self.logger.info(
                "********************Test manager Login With Valid Username And Password successfully login********************************")

            self.manager_dashboard.forecast_date(ReadConfig.get_forecast_date())
            # self.manager_dashboard.start_date(ReadConfig.get_start_date())
            # self.manager_dashboard.end_date(ReadConfig.get_end_date())
            self.manager_dashboard.windvariance_chart_submit()
            self.filename = self.files.get_download_dir() + '/' + self.manager_dashboard.gpalli_variance_csv
            if os.path.isfile(self.filename):

                os.remove((self.filename))
            else:
                print('no file')
            self.manager_dashboard.windvariance_download()

            if os.path.isfile(self.filename):
                assert True
                self.logger.info("**********************In manager dashboard Actual v/s Forecasted chart file downloaded succesfully*******************************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "actual_forecast_downloaded.png")
                self.logger.info("*************************In manager dashboard Actual v/s Forecasted chart file downloaded is failed*************************************")
                assert False
            df = pd.read_csv(r'C:\Users\sanjeev\PycharmProjects\AtriaTesting-2.0\Downloads\gvpalli_variance.csv')
            df_actual = df['Actual Power (MWh)'].sum()
            df_actual = str(df_actual)
            df_forecast = df['Forecasted Power (MWh)'].sum()
            df_forecast=str(df_forecast)
            actual_power=self.manager_dashboard.total_actual_power_find()
            actual_power=actual_power.split(" ")
            forecast_power=self.manager_dashboard.total_forecast_power_find()
            forecast_power=forecast_power.split(" ")






            if df_actual == actual_power[0]:
                assert True
                self.logger.info("*************************downloaded actual and UI actual power generation are matched successfully****************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "actualvsuiactual_downloaded.png")
                self.logger.info(
                    "****************************downloaded actual and UI actual power generation are not  matched ********************************")
                assert False

            if df_forecast == forecast_power[0]:
                assert True
                self.logger.info("*************************downloaded forecast and UI forcast power generation are matched successfully****************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "forecast_vs_uiforecast_downloaded.png")
                self.logger.info(
                    "****************************downloaded forecast and UI forecast power generation are not  matched ********************************")
                assert False


            if os.path.isfile('gvpalli_forecasted.csv'):

                os.remove((r'C:\Users\sanjeev\PycharmProjects\AtriaTesting-2.0\Downloads\gvpalli_forecasted.csv'))
            else:
                print('no file')


            self.manager_dashboard.windform_forecast_button()
            self.manager_dashboard.wind_forecst_download()
            self.file = DirectoryPath()
            self.filename = self.file.get_download_dir() + '/' + self.manager_dashboard.gvpalli_forecasted_csv
            df = pd.read_csv(self.filename)
            df_forecast_45 = df['Forecasted Power (MWh)'].sum()
            df_forecast_45 = str(df_forecast_45)
            forecast_45_power=self.manager_dashboard.windform_future_45_forecast()
            forecast_45_power=forecast_45_power.split(" ")
            if df_forecast_45 == forecast_45_power[0]:
                assert True
                self.logger.info("*************************downloaded 45_forecast and UI 45_forcast power generation are matched successfully****************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "45forecast_vs_ui_45forecast_downloaded.png")
                self.logger.info(
                    "****************************downloaded 45_forecast and UI 45_forecast power generation are not  matched ********************************")
                assert False
            if os.path.isfile(r'C:\Users\sanjeev\PycharmProjects\AtriaTesting-2.0\Downloads\gvpalli_forecasted.csv'):

                os.remove(self.filename)
            else:
                print('no file')

            self.manager_dashboard.windform_forecast_date(ReadConfig.get_future_forecast_date())
            self.manager_dashboard.windform_forecast_button()

            self.manager_dashboard.wind_forecst_download()
            self.file = DirectoryPath()
            self.filename = self.file.get_download_dir() + '/' + self.manager_dashboard.gvpalli_forecasted_csv
            if os.path.isfile(self.filename):
                assert True
                self.logger.info("**********************In manager dashboard 45 forecast file downloaded succesfully*******************************")
            else:
                self.driver.save_screenshot(
                    "../Screenshots/" + "forecast_45_downloaded.png")
                self.logger.info("*************************In manager dashboard 45 forecast chart file downloaded is failed*************************************")
                assert False






        else:
            self.driver.save_screenshot(
                "../Screenshots/" + "test_admin_login_with_valid_username_and_valid_password.png")
            self.logger.info(
                "******************** manager Login With Valid Username And Password Failed********************************")
            self.driver.close()
            assert False
