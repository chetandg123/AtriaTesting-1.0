import logging
class managerLogGen:
    @staticmethod
    def logen():
        logging.basicConfig(filename="../Logs/managerLogin_automationlogs.log",format='%(asctime)s: %(levelname)s:%(message)s',datefmt='%m%d%Y %I:%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger