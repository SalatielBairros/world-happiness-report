import logging
from lib.logging_configuration import configurate_logging

class Commands:
    def __init__(self) -> None:
        self.commands = []
        configurate_logging()

    def add_command(self, command):
        self.commands.append(command)
        return self

    def execute(self):
        for command in self.commands:
            logging.info(f"Executando comando: {command.__name__}")
            command().execute()
