import wget
import os

endpoints = [
    {
        'route':'score-regression/knn/evaluate',
        'filename': 'knn_regression_evaluation.json'
    },
    {
        'route':'score-regression/random-forest/evaluate',
        'filename': 'rf_regression_evaluation.json'
    },
    {
        'route':'region-classification/knn/evaluate',
        'filename': 'knn_region_classification_evaluation.json'
    },
    {
        'route':'region-classification/random-forest/evaluate',
        'filename': 'rf_region_classification_evaluation.json'
    },
    {
        'route':'region-classification/knn/balanced/evaluate',
        'filename': 'knn_region_classification_balanced_evaluation.json'
    },
    {
        'route':'region-classification/random-forest/balanced/evaluate',
        'filename': 'rf_region_classification_balanced_evaluation.json'
    },
]

def download_sample(route:str, filename: str):
    url = f'http://localhost:8000/{route}'
    base_path = './docs/api_return_samples'
    save_path = f'{base_path}/{filename}'
    if(os.path.exists(save_path)):
        os.remove(save_path)
    wget.download(url, save_path)

for endpoint in endpoints:
    download_sample(endpoint['route'], endpoint['filename'])
    print(f'Downloaded {endpoint["filename"]}')