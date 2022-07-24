import logging
from repository.local_storage_repository import LocalStorageRepository

class Commands:
    def __init__(self, repository: LocalStorageRepository) -> None:
        self.commands = []
        self.repository = repository
        self.dataset = None

    def add_command(self, command):
        self.commands.append(command)
        return self

    def execute_and_save(self):
        self.dataset = self.__load_data__()
        for command in self.commands:
            logging.info(f"Executando comando: {command.__name__}")
            self.dataset = command(self.dataset).execute()

        self.repository.save_augmented_dataset(self.dataset)
        return self.dataset

    def __load_data__(self):
        return self.repository.get_processed_dataset()