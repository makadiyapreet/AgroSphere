import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker for realistic data
fake = Faker()

# Set random seed for reproducibility
random.seed(42)

# Define record counts
record_counts = {
    'Farms': 36,
    'Fields': 120,
    'Crops': 18,
    'Crop_Plantings': 480,
    'Livestock': 360,
    'Weather_Readings': 4200,
    'Soil_Samples': 1200,
    'Irrigation_Systems': 48,
    'Pesticide_Applications': 810,
    'Harvests': 528,
    'Storage_Facilities': 12,
    'Processing_Plants': 9,
    'Distribution_Centers': 11,
    'Retail_Outlets': 96,
    'Product_Shipments': 2100
}

# Helper functions
def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Data generation for each table
data = {}

# 1. Farms
farms = []
for i in range(1, record_counts['Farms'] + 1):
    farms.append({
        'farm_id': i,
        'farm_name': fake.company() + ' Farm',
        'location': fake.state(),
        'owner': fake.name(),
        'size_acres': random.randint(100, 1000),
        'carbon_footprint_tons': round(random.uniform(1.0, 10.0), 2)
    })
data['Farms'] = pd.DataFrame(farms)

# 2. Fields
fields = []
for i in range(1, record_counts['Fields'] + 1):
    fields.append({
        'field_id': i,
        'farm_id': random.randint(1, record_counts['Farms']),
        'field_name': f'Field {random.choice(["North", "South", "East", "West"])}',
        'area_acres': random.randint(20, 200),
        'soil_type': random.choice(['Loam', 'Clay', 'Sandy', 'Silt'])
    })
data['Fields'] = pd.DataFrame(fields)

# 3. Crops
crops = []
for i in range(1, record_counts['Crops'] + 1):
    crops.append({
        'crop_id': i,
        'crop_name': random.choice(['Corn', 'Wheat', 'Soybean', 'Rice', 'Barley']),
        'growth_days': random.randint(90, 180),
        'season': random.choice(['Summer', 'Winter', 'Spring']),
        'predicted_price_per_ton': round(random.uniform(150.0, 300.0), 2),
        'profit_estimate': round(random.uniform(10000, 50000), 2)
    })
data['Crops'] = pd.DataFrame(crops)

# 4. Crop_Plantings
crop_plantings = []
for i in range(1, record_counts['Crop_Plantings'] + 1):
    planting_date = random_date(2024, 2025)
    growth_days = int(data['Crops'].iloc[random.randint(0, record_counts['Crops'] - 1)]['growth_days'].item())
    harvest_date = planting_date + timedelta(days=growth_days)
    crop_plantings.append({
        'planting_id': i,
        'field_id': random.randint(1, record_counts['Fields']),
        'crop_id': random.randint(1, record_counts['Crops']),
        'planting_date': planting_date.strftime('%Y-%m-%d'),
        'expected_harvest_date': harvest_date.strftime('%Y-%m-%d'),
        'predicted_yield_tons': round(random.uniform(50.0, 200.0), 2)
    })
data['Crop_Plantings'] = pd.DataFrame(crop_plantings)

# 5. Livestock
livestock = []
for i in range(1, record_counts['Livestock'] + 1):
    livestock.append({
        'livestock_id': i,
        'farm_id': random.randint(1, record_counts['Farms']),
        'animal_type': random.choice(['Cattle', 'Chickens', 'Pigs', 'Sheep']),
        'count': random.randint(10, 500),
        'birth_date': random_date(2023, 2024).strftime('%Y-%m-%d')
    })
data['Livestock'] = pd.DataFrame(livestock)

# 6. Weather_Readings
weather_readings = []
for i in range(1, record_counts['Weather_Readings'] + 1):
    weather_readings.append({
        'reading_id': i,
        'farm_id': random.randint(1, record_counts['Farms']),
        'date': random_date(2024, 2025).strftime('%Y-%m-%d'),
        'temperature_f': round(random.uniform(30.0, 100.0), 2),
        'precipitation_in': round(random.uniform(0.0, 2.0), 2)
    })
data['Weather_Readings'] = pd.DataFrame(weather_readings)

# 7. Soil_Samples
soil_samples = []
for i in range(1, record_counts['Soil_Samples'] + 1):
    soil_samples.append({
        'sample_id': i,
        'field_id': random.randint(1, record_counts['Fields']),
        'date': random_date(2024, 2025).strftime('%Y-%m-%d'),
        'ph_level': round(random.uniform(5.0, 8.0), 1),
        'nitrogen_ppm': random.randint(10, 50),
        'health_score': random.randint(50, 100),
        'recommendation_text': random.choice(['Add lime', 'Increase nitrogen', 'Reduce watering'])
    })
data['Soil_Samples'] = pd.DataFrame(soil_samples)

# 8. Irrigation_Systems
irrigation_systems = []
for i in range(1, record_counts['Irrigation_Systems'] + 1):
    irrigation_systems.append({
        'system_id': i,
        'field_id': random.randint(1, record_counts['Fields']),
        'type': random.choice(['Drip', 'Sprinkler', 'Flood']),
        'install_date': random_date(2020, 2024).strftime('%Y-%m-%d'),
        'water_usage_gallons': random.randint(1000, 10000),
        'optimization_tip': random.choice(['Reduce by 10%', 'Schedule at night', 'Check leaks'])
    })
data['Irrigation_Systems'] = pd.DataFrame(irrigation_systems)

# 9. Pesticide_Applications
pesticide_applications = []
for i in range(1, record_counts['Pesticide_Applications'] + 1):
    pesticide_applications.append({
        'application_id': i,
        'field_id': random.randint(1, record_counts['Fields']),
        'pesticide_name': random.choice(['Glyphosate', 'Permethrin', 'Malathion']),
        'date': random_date(2024, 2025).strftime('%Y-%m-%d'),
        'amount_lbs': round(random.uniform(1.0, 5.0), 2),
        'pest_type': random.choice(['Aphids', 'Locusts', 'Weevils']),
        'severity_level': random.randint(1, 5)
    })
data['Pesticide_Applications'] = pd.DataFrame(pesticide_applications)

# 10. Harvests (Fixed)
harvests = []
for i in range(1, record_counts['Harvests'] + 1):
    # Randomly select a planting_id from Crop_Plantings (1 to 480)
    planting_id = random.randint(1, record_counts['Crop_Plantings'])
    planting = data['Crop_Plantings'].loc[data['Crop_Plantings']['planting_id'] == planting_id].iloc[0]
    harvest_date = datetime.strptime(planting['expected_harvest_date'], '%Y-%m-%d')
    planned_date = harvest_date - timedelta(days=random.randint(5, 10))
    harvests.append({
        'harvest_id': i,
        'planting_id': planting_id,
        'date': harvest_date.strftime('%Y-%m-%d'),
        'yield_tons': random.randint(50, 200),
        'planned_date': planned_date.strftime('%Y-%m-%d'),
        'logistics_note': random.choice(['Use Truck A', 'Coordinate with Distro', 'Store in Barn'])
    })
data['Harvests'] = pd.DataFrame(harvests)

# 11. Storage_Facilities
storage_facilities = []
for i in range(1, record_counts['Storage_Facilities'] + 1):
    storage_facilities.append({
        'facility_id': i,
        'farm_id': random.randint(1, record_counts['Farms']),
        'capacity_tons': random.randint(200, 1000),
        'location': f'Barn {i}'
    })
data['Storage_Facilities'] = pd.DataFrame(storage_facilities)

# 12. Processing_Plants
processing_plants = []
for i in range(1, record_counts['Processing_Plants'] + 1):
    processing_plants.append({
        'plant_id': i,
        'name': fake.company() + ' Processing',
        'location': fake.state(),
        'capacity_tons_per_day': random.randint(100, 300),
        'certification_type': random.choice(['USDA Organic', 'HACCP', 'ISO 22000']),
        'cert_expiry_date': random_date(2025, 2026).strftime('%Y-%m-%d'),
        'facility_id': random.randint(1, record_counts['Storage_Facilities'])

    })
data['Processing_Plants'] = pd.DataFrame(processing_plants)

# 13. Distribution_Centers
distribution_centers = []
for i in range(1, record_counts['Distribution_Centers'] + 1):
    distribution_centers.append({
        'center_id': i,
        'name': f'Distro {chr(65 + i - 1)}',
        'location': fake.state(),
        'capacity_units': random.randint(5000, 15000)
    })
data['Distribution_Centers'] = pd.DataFrame(distribution_centers)

# 14. Retail_Outlets
retail_outlets = []
for i in range(1, record_counts['Retail_Outlets'] + 1):
    retail_outlets.append({
        'outlet_id': i,
        'name': fake.company() + ' Store',
        'location': fake.city(),
        'type': random.choice(['Grocery', 'Market', 'Co-op']),
        'certification_type': random.choice(['USDA Organic', 'HACCP', 'Fair Trade']),
        'cert_expiry_date': random_date(2025, 2026).strftime('%Y-%m-%d'),
        'center_id': random.randint(1, record_counts['Distribution_Centers'])

    })
data['Retail_Outlets'] = pd.DataFrame(retail_outlets)

# 15. Product_Shipments
product_shipments = []
for i in range(1, record_counts['Product_Shipments'] + 1):
    harvest_date = datetime.strptime(data['Harvests'].iloc[random.randint(0, record_counts['Harvests'] - 1)]['date'], '%Y-%m-%d')
    shipment_date = harvest_date + timedelta(days=random.randint(1, 10))
    product_shipments.append({
        'shipment_id': i,
        'harvest_id': random.randint(1, record_counts['Harvests']),
        'destination_id': random.randint(1, record_counts['Distribution_Centers']),
        'date': shipment_date.strftime('%Y-%m-%d'),
        'weight_tons': random.randint(20, 150),
        'traceability_code': f'TRC-{i:04d}'
    })
data['Product_Shipments'] = pd.DataFrame(product_shipments)

# Save to CSV files
output_dir = 'agricultural_data'
os.makedirs(output_dir, exist_ok=True)
for table_name, df in data.items():
    df.to_csv(f'{output_dir}/{table_name}.csv', index=False)
    print(f'Saved {table_name} with {len(df)} records to {output_dir}/{table_name}.csv')

# Verify total records
total_records = sum(len(df) for df in data.values())
print(f'Total records generated: {total_records}')