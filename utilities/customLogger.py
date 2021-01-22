import logging
class LogGen:

    @staticmethod
    def logen():
        logging.basicConfig(filename="../Logs/admin_automation.log",filemode='a',format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def ceo_logs():
        logging.basicConfig(filename="../Logs/ceo_screens.log", format='%(asctime)s: %(levelname)s:%(message)s',
                            datefmt='%m%d%Y %I:%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger