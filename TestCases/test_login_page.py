from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Atria_Login_Page:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logen()

