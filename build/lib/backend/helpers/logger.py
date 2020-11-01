import logging
from datetime import datetime

from colorama import Fore


class Logger:

    @staticmethod
    def LogInfo(message, do_print=False):
        """
        logging and colouring command line messages during the tests execution
        :rtype: object
        """
        now = datetime.now()
        message = f"{Fore.GREEN}[{now}] {message}"
        logging.info(f"{Fore.GREEN}[{now}] {message}")
        if do_print:
            print(f"{Fore.GREEN}[{now}] {message}")
