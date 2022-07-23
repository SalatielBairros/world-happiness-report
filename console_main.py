from services.region_service import RegionService

df = RegionService().__merge_kaggle_datasets__()
print(df)