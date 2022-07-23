class DatasetConstants:
    PAST_DATA_COLUMNS = ['country', 'year', 'score', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption', 'positive_affect', 'negative_affect']
    DATA_2021_COLUMNS = ['country', 'region', 'score', 'std_score', 'upperwhisker', 'lowerwhisker', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption']

class EnvironmentVariables:
    SEED = 42
    ORIGINAL_URLS = ["OriginalHistoricDataUrl", 'Data2021Url', 'Kaggle2015Url', 'Kaggle2016Url', 'CountriesUsaDatabaseUrl']