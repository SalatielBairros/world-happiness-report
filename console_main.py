from data_combination.data_combination_commands import execute_data_combination
from data_preparation.data_preparation_commands import execute_data_preparation

df = execute_data_combination()
df = execute_data_preparation()

print(df)