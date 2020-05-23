# author  : Charles Cavin <charles@cavinAI.com>
# license : MIT

import logging
from datetime import datetime


class PrintAndLog:

    lvl = {"debug": logging.DEBUG,
           "info": logging.INFO,
           "warning": logging.WARNING,
           "error": logging.ERROR,
           "critical": logging.CRITICAL
           }

    def __init__(self,
                 log_filename,
                 log_format="%(levelname)s:%(asctime)s:%(message)s",
                 log_datefmt="%H:%M:%S",
                 log_level="info"):

        log_filename += f"{datetime.today()}"

        log_level = self.lvl[log_level]

        logging.basicConfig(
            filename=log_filename,
            level=log_level,
            filemode="w",
            format=log_format,
            datefmt=log_datefmt
        )

    def print(self, msg, log_level="info", end=False, log=True, prt=True):
        if prt is True and end is not True:
            print(msg)
        else:
            print(msg, end=' ')

        if log is True:
            logging.log(self.lvl[log_level], msg)
