import logging
class LogGen:

    @staticmethod
    def logen():
        logging.basicConfig(filename="../Logs/admin_automation.log",filemode='a',format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger