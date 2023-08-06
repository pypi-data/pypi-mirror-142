#! /usr/bin/python3.9
"Script for logging encryption/decryptions, login/logout dates, and password changes for the Revenant app."

import os
import logging
from pathlib import Path

class Log:
    """
    A logging class.

    parameters:
    `log_file_name`: The file to be logging to. Do not provide as a full path.
        The class will automatically append the file to the current working directory.
    """


    def __init__(self, log_file_name:str) -> None:
        if os.path.isabs(log_file_name) is True:
            self.log_file_name = Path(log_file_name)
        else:
            self.log_file_name = Path.cwd() / log_file_name
        self.level = logging.DEBUG
        self.setlog = logging.basicConfig(filename=self.log_file_name, format="%(asctime)s : %(name)s - %(levelname)s - %(message)s")


    def log_exists(self) -> bool:
        "Checks if a log file exists. Returns a boolean value."
        file_name_validity = os.path.exists(self.log_file_name)
        return file_name_validity


    def create_log(self) -> int:
        "Creates a log file."
        with open (self.log_file_name, "w+") as file:
            file.write("log file created.")
        return 0
        

    def audit(self, keywords:list) -> int:
        """
        A method for removing logged objects containing words in the `keywords` list.
        """
        with open (self.log_file_name, "w+") as file:
            lines = file.readlines()
            for word in keywords:
                for line in lines:
                    if word not in line:
                        file.write(line)
        return 0


    def log(self, message:str, type_:str) -> int:
        """
        A method for simplifing log writes with the builtin `logging` module.
       
       
        Parameters:
        `message`: The message to be written to the log file
        `type_`: What level to log the message as.
            Possible types:

            'DEBUG'

            'INFO'
            
            'WARNING'
            
            'ERROR'

            'CRITICAL'

        Returns 0 if a valid type was detected; otherwise returns 1.
        """
        if type_ == "DEBUG":
            logging.debug(msg=message)
            return 0
        elif type_ == "INFO":
            logging.info(msg=message)
            return 0
        elif type_ == "WARNING":
            logging.warning(msg=message)
            return 0
        elif type_ == "ERROR":
            logging.error(msg=message)
            return 0
        elif type_ == "CRITICAL":
            logging.critical(msg=message)
            return 0
        else:
            return 1