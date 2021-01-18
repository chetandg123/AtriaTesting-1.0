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
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_manager_Username():
        username = config.get('common info', 'manager_user')
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

