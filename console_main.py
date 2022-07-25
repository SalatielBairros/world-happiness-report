from services.model_service import ModelService
from environment.env_configuration import prepare_environment
from app.entities.request.country_data import CountryData
from models.classification.knn_classifier_model import KnnClassifierModel
from models.regression.knn_model import KnnModel

prepare_environment()

#brazil 2013
#cat_region,score,gdp,social_support,freedom,generosity,corruption,positive_affect,negative_affect,scaled_hle
#4,7.14028263092041,9.667767524719238,0.9104217290878296,0.7848149538040161,-0.0946823805570602,0.7069541811943054,0.8176620602607727,0.2756677567958832,0.6468571254185268

data = CountryData(
    cat_region=4,
    score=7.14028263092041,
    gdp=9.667767524719238,
    social_support=0.9104217290878296,
    freedom=0.7848149538040161,
    generosity=-0.0946823805570602,
    corruption=0.7069541811943054,
    positive_affect=0.8176620602607727,
    negative_affect=0.2756677567958832,
    hle=65.27999877929688)

classification_model = KnnClassifierModel()
regression_model = KnnModel()

prediction_result = ModelService(regression_model, classification_model).get_prediction_results(data)
print(prediction_result.dict())