import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class/method from where the method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default log all messages
    logger.setLevel(logging.DEBUG)

    # Create one log file - Append all together
    fileHandler = logging.FileHandler("SN_automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
