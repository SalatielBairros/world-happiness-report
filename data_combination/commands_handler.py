import logging
from repository.local_storage_repository import LocalStorageRepository
from data_combination.dataset_join import DatasetsJoin

class Commands:
    def __init__(self, repository: LocalStorageRepository) -> None:
        self.commands = []
        self.repository = repository
        self.historic_data = None
        self.data_2021 = None

    def add_command(self, command):
        self.commands.append(command)
        return self

    def execute_and_save(self):
        self.__load_data__()

        for command in self.commands:
            logging.info(f"Executando comando: {command.__name__}")
            self.historic_data, self.data_2021 = command(self.historic_data, self.data_2021).execute()

        logging.info('Juntando os datasets...')
        joined_dataset = DatasetsJoin(self.historic_data, self.data_2021).execute()
        self.repository.save_joined_dataset(joined_dataset)
        return joined_dataset

    def __load_data__(self):
        self.historic_data = self.repository.get_original_historic_data()
        self.data_2021 = self.repository.get_original_2021_data()