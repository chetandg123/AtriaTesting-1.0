import configparser
config=configparser.RawConfigParser()
config.read("../Configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','admin_username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','admin_password')
        return password

    @staticmethod
    def get_manager_Username():
        username = config.get('common info', 'manager_username')
        return username

    @staticmethod
    def get_manager_Password():
        password = config.get('common info', 'manager_password')
        return password

    @staticmethod
    def get_ceo_Username():
        username = config.get('common info', 'ceo_user')
        return username

    @staticmethod
    def get_ceo_Password():
        password = config.get('common info', 'ceo_password')
        return password


    @staticmethod
    def get_invalid_Username():
        username = config.get('common info', 'invalid_username')
        return username

    @staticmethod
    def get_invalid_Password():
        password = config.get('common info', 'invalid_password')
        return password

    @staticmethod
    def getmanager_username():
        manager_username = config.get('common info', 'manager_username')
        return manager_username

    @staticmethod
    def getmanager_password():
        manager_password = config.get('common info', 'manager_password')
        return manager_password

    @staticmethod
    def getinvalidmanger_name():
        invalid_manager_name = config.get('common info', 'invalid_manager_name')
        return invalid_manager_name

    @staticmethod
    def getinvalidmanager_password():
        invalid_manager_password = config.get('common info', 'invalid_manager_password')
        return invalid_manager_password

    @staticmethod
    def getcomment_add():
        comment_add = config.get('common info', 'comment_add')
        return comment_add

    @staticmethod
    def getedit_input():
        edit_input = config.get('common info', 'edit_comment')
        return edit_input


    @staticmethod
    def get_forecast_date():
        dates = config.get('common info', 'forecast_variance_date')
        return dates

    @staticmethod
    def get_future_forecast_date():
        dates = config.get('common info', 'forecast_date')
        return dates




