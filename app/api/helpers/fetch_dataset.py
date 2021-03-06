import json
from os import path

import pandas as pd


class FetchDataset:

  def __init__(self):
    self.input_file = r'/app/app/api/datasets/complete_dataset_region.csv'

  def fetched_dataset(self):
    if (path.exists(self.input_file)):
      dataset = self.read_csv_dataset(self.input_file)
      json_dataset = self.format_dataset_to_json(dataset)
      return json_dataset
    else:
      return {
        "message": "Não há dataset gerado."
      }

  def read_csv_dataset(self, dataset):
    return  pd.read_csv(dataset, names=(
      "country",
      "region",
      "score",
      "gdp",
      "social_support",
      "hle",
      "freedom",
      "generosity",
      "corruption",
      "positive_affect",
      "negative_affect",
      "year"
    ))

  def format_dataset_to_json(self, dataset):
    json_dataset = json.loads(json.dumps(list(dataset.T.to_dict().values())))
    json_dataset.pop(0)
    return json_dataset
