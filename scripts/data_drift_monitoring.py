import os
import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from azure.storage.blob import BlobServiceClient

# Load the dataset
data = pd.read_csv("../data/marketing_campaign.csv",sep='\t')

reference_data = data.sample(frac=0.7, random_state=1)
reference_data.to_csv('../data/reference_data.csv', index=False)

new_data = data.drop(reference_data.index)
new_data.to_csv('../data/new_data.csv', index=False)

# Load reference (training) data and new data
reference_data = pd.read_csv("../data/reference_data.csv")
new_data = pd.read_csv("../data/new_data.csv")

# Define column mapping (adjust according to your dataset)
column_mapping = ColumnMapping(
    numerical_features=['Year_Birth', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth'],
    categorical_features=['Education', 'Marital_Status', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response'] 
)


# Create a report and add DataDriftPreset
data_drift_report = Report(metrics=[DataDriftPreset()])
data_drift_report.run(reference_data=reference_data, current_data=new_data, column_mapping=column_mapping)

# Save the report to a JSON file
report_path = "../reports/data_drift_report.json"
if not os.path.exists("reports"):
    os.makedirs("reports")
data_drift_report.save_json(report_path)

from dotenv import load_dotenv
load_dotenv()

# Upload the report to Azure Blob Storage
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="reports/data_drift_report.json")

with open(report_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("Data drift report uploaded to Azure Blob Storage.")
