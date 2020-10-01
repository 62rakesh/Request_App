import logging


class LogGen:

    logging.basicConfig(filename=".\\Logs\\info.log",
                        format='%(asctime)s: %(levelname)s: %(message)s:')

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


