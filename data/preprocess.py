import pandas as pd
import re
from numpy import int64, float64

## Constants
PREFIX = { 'K': 10**3, 'M': 10**6 }
OUTPUT_FILE_NAME = './output/preprocessed_challenge_data.csv'
D_TYPES = {
	'id': int64, 'bathrooms': float64, 'bedrooms': float64, 'home_size': int64, 'last_sold_price': int64, 'price': int64, 'property_size': int64, 'rent_price': int64, 'rentzestimate_amount': int64, 'tax_value': int64, 'tax_year': int64, 'year_built': int64, 'zestimate_amount': int64
}
DATE_COLS = ['last_sold_date', 'rentzestimate_last_updated', 'zestimate_last_updated']

## Maps a humanized price e.g 1.25M to a float e.g 1,250,000.0 for search/filtering purposess
def humanized_to_float (humanized_price):
	price_components = re.findall(r'[\d\.\d]+|[KM]', humanized_price)
	return float(price_components[0]) * PREFIX[price_components[1]]

## Read csv into dataframe
zillow_df = pd.read_csv('./raw/challenge_data.csv', parse_dates=DATE_COLS, converters={'price': humanized_to_float}, na_values=[''])

## Rename zillow_id to id and set as df index
zillow_df = zillow_df.rename(columns = {'zillow_id': 'id'})
zillow_df.set_index('id', inplace=True)

## Change types for Integer columns
zillow_df['tax_year'] = zillow_df['tax_year'].astype('Int64')
zillow_df['year_built'] = zillow_df['year_built'].astype('Int64')

## Write out new csv
zillow_df.to_csv(OUTPUT_FILE_NAME, encoding='utf-8')