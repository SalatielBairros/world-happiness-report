from services.region_service import RegionService

df = RegionService().merge_kaggle_datasets()
print(df)