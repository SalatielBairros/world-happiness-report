from data_combination.data_combination_commands import execute_data_combination
from data_preparation.data_preparation_commands import execute_data_preparation
from feature_engineering.feature_engineering_commands import execute_feature_engineering
from environment.env_configuration import preparing_environment

preparing_environment()

df = execute_data_combination()
df = execute_data_preparation()
df = execute_feature_engineering()

print(df)