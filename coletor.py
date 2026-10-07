import requests
import pandas as pd
from datetime import date
from sqlalchemy import create_engine

# 1. Fetch today's electricity prices for Rogaland (NO2 region) from the public API
today_date = date.today().strftime("%Y/%m-%d")
api_url = f"https://www.hvakosterstrommen.no/api/v1/prices/{today_date}_NO2.json"

response = requests.get(api_url)
raw_data = response.json()

# 2. Process and clean the data using Pandas
df = pd.DataFrame(raw_data)
df['time_start'] = pd.to_datetime(df['time_start'])
df['hour'] = df['time_start'].dt.hour
df['price_nok_per_kwh'] = df['NOK_per_kWh']

processed_df = df[['hour', 'price_nok_per_kwh', 'EUR_per_kWh']]

# 3. Save the data into a local SQLite database
db_engine = create_engine('sqlite:///rogaland_energy.db')
processed_df.to_sql('energy_prices', con=db_engine, if_exists='replace', index=False)

# 4. Query the SQLite database for the 3 cheapest hours of the day
sql_query = """
SELECT hour, price_nok_per_kwh 
FROM energy_prices 
ORDER BY price_nok_per_kwh ASC 
LIMIT 3;
"""

cheapest_hours = pd.read_sql_query(sql_query, db_engine)
print("=== CHEAPEST ELECTRICITY HOURS TODAY IN ROGALAND (NO2) ===")
print(cheapest_hours)