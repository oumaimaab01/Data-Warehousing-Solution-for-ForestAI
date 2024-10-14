import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate Date Dimension
def generate_date_dimension(start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date)
    date_dim = pd.DataFrame({
        'DateKey': range(1, len(date_range) + 1),
        'FullDate': date_range,
        'Year': date_range.year,
        'Quarter': date_range.quarter,
        'Month': date_range.month,
        'Day': date_range.day
    })
    return date_dim

# Generate Region Dimension
def generate_region_dimension():
    regions = ['North', 'South', 'East', 'West']
    region_dim = pd.DataFrame({
        'RegionKey': range(1, len(regions) + 1),
        'RegionName': regions,
        'RegionDescription': [f'{region} Region' for region in regions]
    })
    return region_dim

# Generate Species Dimension
def generate_species_dimension():
    species = ['Pine', 'Birch', 'Spruce', 'Deciduous']
    species_dim = pd.DataFrame({
        'SpeciesKey': range(1, len(species) + 1),
        'SpeciesName': species,
        'SpeciesDescription': [f'{sp} Species' for sp in species]
    })
    return species_dim

# Generate Model Dimension
def generate_model_dimension(n_models):
    model_dim = pd.DataFrame({
        'ModelVersionKey': range(1, n_models + 1),
        'ModelVersion': [f'v{100+i}' for i in range(n_models)],
        'ModelDescription': [f'Model version {100+i}' for i in range(n_models)],
        'CreationDate': [datetime.now() - timedelta(days=random.randint(1, 1000)) for _ in range(n_models)]
    })
    return model_dim

# Generate Data Source Dimension
def generate_data_source_dimension():
    sources = ['GroundTruth', 'ClientEstimate', 'ForestAIPrediction']
    data_source_dim = pd.DataFrame({
        'DataSourceKey': range(1, len(sources) + 1),
        'DataSourceName': sources,
        'DataSourceDescription': [f'{source} Source' for source in sources]
    })
    return data_source_dim

# Generate Client Dimension
def generate_client_dimension(n_clients):
    clients = [f'Client_{i+1}' for i in range(n_clients)]
    industries = ['Forestry', 'Agriculture', 'Construction', 'Mining']
    client_dim = pd.DataFrame({
        'ClientID': range(1, n_clients + 1),
        'ClientName': clients,
        'Industry': [random.choice(industries) for _ in range(n_clients)],
        'Region': [random.choice(['North', 'South', 'East', 'West']) for _ in range(n_clients)]
    })
    return client_dim

# Generate Model Performance Facts
def generate_model_performance_facts(date_dim, region_dim, species_dim, model_dim, data_source_dim, n_records):
    records = []
    for _ in range(n_records):
        record = {
            'DateKey': random.choice(date_dim['DateKey']),
            'RegionKey': random.choice(region_dim['RegionKey']),
            'SpeciesKey': random.choice(species_dim['SpeciesKey']),
            'ModelVersionKey': random.choice(model_dim['ModelVersionKey']),
            'DataSourceKey': random.choice(data_source_dim['DataSourceKey']),
            'PredictedVolume': round(random.uniform(10, 100), 2),
            'PredictedHeight': round(random.uniform(5, 30), 2),
            'PredictedDiameter': round(random.uniform(10, 60), 2),
            'ErrorMetric': round(random.uniform(0, 10), 2),
            'ClientEstimate': round(random.uniform(10, 100), 2),
            'GroundTruth': round(random.uniform(10, 100), 2)
        }
        records.append(record)
    return pd.DataFrame(records)

# Generate Client Comparison Facts
def generate_client_comparison_facts(client_dim, model_dim, species_dim, date_dim, n_records):
    records = []
    for _ in range(n_records):
        record = {
            'ClientID': random.choice(client_dim['ClientID']),
            'ModelVersionKey': random.choice(model_dim['ModelVersionKey']),
            'PredictionDate': random.choice(date_dim['FullDate']),
            'SpeciesKey': random.choice(species_dim['SpeciesKey']),
            'PredictedVolume': round(random.uniform(10, 100), 2),
            'ClientEstimatedVolume': round(random.uniform(10, 100), 2),
            'ErrorMetric': round(random.uniform(0, 10), 2)
        }
        records.append(record)
    return pd.DataFrame(records)

# Parameters
start_date = '2020-01-01'
end_date = '2023-12-31'
n_models = 10
n_clients = 15
n_records = 1000

# Generate Dimensions
date_dim = generate_date_dimension(start_date, end_date)
region_dim = generate_region_dimension()
species_dim = generate_species_dimension()
model_dim = generate_model_dimension(n_models)
data_source_dim = generate_data_source_dimension()
client_dim = generate_client_dimension(n_clients)

# Generate Facts
model_performance_facts = generate_model_performance_facts(date_dim, region_dim, species_dim, model_dim, data_source_dim, n_records)
client_comparison_facts = generate_client_comparison_facts(client_dim, model_dim, species_dim, date_dim, n_records)

# Save to CSV
date_dim.to_csv('date_dimension.csv', index=False)
region_dim.to_csv('region_dimension.csv', index=False)
species_dim.to_csv('species_dimension.csv', index=False)
model_dim.to_csv('model_dimension.csv', index=False)
data_source_dim.to_csv('data_source_dimension.csv', index=False)
client_dim.to_csv('client_dimension.csv', index=False)
model_performance_facts.to_csv('model_performance_facts.csv', index=False)
client_comparison_facts.to_csv('client_comparison_facts.csv', index=False)

print("Datasets generated and saved as CSV files.")
