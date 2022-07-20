from os import path
import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class ScorePrediction:

  def __init__(self):
    self.input_file = r'/app/app/api/datasets/complete_dataset_region.csv'

  def construct_model(self):
    if (path.exists(self.input_file)):
      dataset = self.read_csv_dataset(self.input_file)
      dataset_model = self.split_data_training_and_test(dataset)
      return dataset_model
    else:
      return {
        "message": "Não há dataset gerado."
      }

  def read_csv_dataset(self, dataset):
    return  pd.read_csv(dataset, usecols=[
      # 'country',
      'year',
      'score',
      'gdp',
      'social_support',
      'hle',
      'freedom'
    ])

  def split_data_training_and_test(self, dataset):
    X = dataset[['gdp', 'social_support', 'hle', 'freedom']]
    y = dataset['score']

    # X = features, y = target variable

    X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size = 0.2, random_state = 0
    )

    scale = StandardScaler()
    dataset = scale.fit_transform(dataset)

    lm = LinearRegression()
    lm.fit(X_train, y_train)

    y_pred = lm.predict(X_test)

    # comparing actual values with predicted values
    current_vs_pred = pd.DataFrame({
      'country': 'em desenvolvimento',
      'current_score': y_test,
      'predicted_score': y_pred
    })

    json_current_vs_pred = json.loads(json.dumps(list(current_vs_pred.T.to_dict().values())))

    print(json_current_vs_pred)
    return json_current_vs_pred
