"""Custom django command to perform data import"""
from django.core.management.base import BaseCommand, CommandError
from athome.zillowchallenge.models import ZListing
import os
import sys
import traceback
import csv

class Command(BaseCommand):
	help = 'Creates new listings from CSV data'

	def add_arguments(self, parser):
		parser.add_argument('data-dir', type=str, help="data directory")

	def parse_field(self, value, type):
		"""Force type for csv field or return None """
		if value:
			return type(value)
		return None
	
	def import_csv_to_db(self, filename):
		"""Read csv file, create instances of Listing model and bulk create"""
		listings = []
		try:
			with open(filename, 'r') as csv_file:
				reader = csv.reader(csv_file, delimiter=',', quotechar='|')
				next(reader)
				for row in reader:
					listing = ZListing(
						id = self.parse_field(row[0], int),
						area_unit = self.parse_field(row[1], str),
						bathrooms = self.parse_field(row[2], float),
						bedrooms = self.parse_field(row[3], float),
						home_size = self.parse_field(row[4], float),
						home_type = self.parse_field(row[5], str),
						last_sold_date = self.parse_field(row[6], str),
						last_sold_price = self.parse_field(row[7], float),
						link = self.parse_field(row[8], str),
						price = self.parse_field(row[9], float),
						property_size = self.parse_field(row[10], float),
						rent_price = self.parse_field(row[11], float),
						rentzestimate_amount = self.parse_field(row[12], float),
						rentzestimate_last_updated = self.parse_field(row[13], str),
						tax_value = self.parse_field(row[14], float),
						tax_year = self.parse_field(row[15], int),
						year_built = self.parse_field(row[16], int),
						zestimate_amount = self.parse_field(row[17], float),
						zestimate_last_updated = self.parse_field(row[18], str),
						address = self.parse_field(row[19], str),
						city = self.parse_field(row[20], str),
						state = self.parse_field(row[21], str),
						zipcode = self.parse_field(row[22], str),
					)
					listings.append(listing)
			## bulk create Listings
			ZListing.objects.bulk_create(listings)
			return len(listings)
		except Exception:
			raise

	def handle(self, *args, **options):
		data_dir = options['data-dir']
		self.stdout.write(self.style.SUCCESS('Attempting to read %s' % data_dir))

		try:
			## Iterate through files in data directory
			for file in os.listdir(data_dir):
				filename = os.fsdecode(file)

				## Filter csv files
				if filename.endswith(".csv"): 
					filename = os.path.join(data_dir, filename)
					self.stdout.write(self.style.SUCCESS('Importing data from %s' % filename))

					## Begin csv to db
					num_of_rows = self.import_csv_to_db(filename)
					if num_of_rows:
						self.stdout.write(self.style.SUCCESS('Sucessfully imported %d rows from %s' % (num_of_rows, filename)))

		except FileNotFoundError:
			raise CommandError('Directory %s does not exist' % data_dir)

		except Exception:
			raise CommandError('%s error \n%s' % (sys.exc_info()[0].__class__.__name__, traceback.format_exc()))
