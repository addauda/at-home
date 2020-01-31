import pandas as pd
import re

## Constants
PREFIX = { 'K': 10**3, 'M': 10**6 }
OUTPUT_FILE_NAME = "./data/preprocessed_challenge_data.csv"

## maps a humanized price e.g 1.25M to a float e.g 1,250,000.0 for search/filtering purposess
def humanized_to_int (humanized_price):
	price = re.findall(r'[\d\.\d]+|[KM]', humanized_price)
	return float(price[0]) * PREFIX[price[1]]

## Read csv into dataframe
zillow_df = pd.read_csv("./raw/challenge_data.csv", parse_dates=True)
zillow_df.set_index('zillow_id', inplace=True)

## Change humanized price to integer
zillow_df['price'] = zillow_df['price'].map(humanized_to_int)

## Write out new csv
zillow_df.to_csv(OUTPUT_FILE_NAME, encoding='utf-8')