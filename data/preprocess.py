"""Pre-processing script for challange data"""
import re
import pandas as pd

## Constants
PREFIX = {'K': 10**3, 'M': 10**6}
OUTPUT_FILE_NAME = './output/preprocessed_challenge_data.csv'
DATE_COLS = ['last_sold_date', 'rentzestimate_last_updated', 'zestimate_last_updated']

def humanized_to_float(humanized_price):
	"""Maps a humanized price e.g 1.25M to a float e.g 1,250,000.0 for search/filtering purposes"""
	price_components = re.findall(r'[\d\.\d]+|[KM]', humanized_price)
	return float(price_components[0]) * PREFIX[price_components[1]]


## Read csv into dataframe
ZILLOW_DF = pd.read_csv(
	'./raw/challenge_data.csv',
	parse_dates=DATE_COLS,
	converters={'price': humanized_to_float},
	na_values=['']
)

## Rename zillow_id to id and set as df index
ZILLOW_DF = ZILLOW_DF.rename(columns={'zillow_id': 'id'})
ZILLOW_DF.set_index('id', inplace=True)

## Change types for Integer columns
ZILLOW_DF['tax_year'] = ZILLOW_DF['tax_year'].astype('Int64')
ZILLOW_DF['year_built'] = ZILLOW_DF['year_built'].astype('Int64')

## Write out new csv
ZILLOW_DF.to_csv(OUTPUT_FILE_NAME, encoding='utf-8')
