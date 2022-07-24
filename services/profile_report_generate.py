import pandas as pd
from pandas_profiling import ProfileReport

class ProfileReportGenerate:
    def __init__(self, dataset, title, file_name):
        self.dataset = dataset
        self.title = title
        self.file_name= file_name

        # MOCK
        # self.processed_datasets_path = '../data/processed/processed_dataset.csv'
        # self.dataset = pd.read_csv(self.processed_datasets_path)
        # self.title = 'WHR TCC - PUC-MG'
        # self.file_name = 'processed-dataset'

        self.generate_view()

    def generate_view(self):
        # GENERATE PROFILE
        profile = ProfileReport(
            pd.DataFrame(self.dataset),
            title=self.title
        )

        # SAVE PROFILE HTML FILE
        profile.to_file(
            f'../views/{self.file_name}.html'
        )

# RUN MOCK
# ProfileReportGenerate()
