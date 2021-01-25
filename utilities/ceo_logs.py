


import logging
class ceoLogGen:
    @staticmethod
    def logen():
        logging.basicConfig(filename="../Logs/ceo_windfarm_logs.log",format='%(asctime)s: %(levelname)s:%(message)s',datefmt='%m%d%Y %I:%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger