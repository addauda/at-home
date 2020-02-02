import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ZListing


class ListingTestCase(APITestCase):

	def setUp(self):
		ZListing.objects.create(
			id = 1,
			price = 21.0,
			address = '1 Way',
			city = 'Toronto',
			state = 'ON',
			zipcode = '11111',
		)
		ZListing.objects.create(
			id = 2,
			price = 22.0,
			address = '2 Way',
			city = 'Toronto',
			state = 'ON',
			zipcode = '22222',
		)
		ZListing.objects.create(
			id = 3,
			price = 23.0,
			address = '3 Way',
			city = 'Toronto',
			state = 'ON',
			zipcode = '33333',
		)

	## Test to retrieve all listings
	def test_get_all_listings(self):
		response = self.client.get('/zlistings/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data['results']), 3) ## Accessing results here due to pagination


	## Test to create a new listing with required parameters present
	def test_create_listing_with_required(self):
		test_listing = {
			'id': 4,
			'area_unit': 'SqFt',
			'bathrooms': 3,
			'bedrooms': 4,
			'home_size': 1470,
			'home_type': 'SingleFamily',
			'last_sold_date': '2016-03-29',
			'last_sold_price': 670000,
			'link': 'https://www.zillow.com/homedetails/5906-Ostrom-Ave-Encino-CA-91316/19977905_zpid/',
			'price': 6000,
			'property_size': 6002,
			'rent_price': '',
			'rentzestimate_amount': 3195,
			'rentzestimate_last_updated': '2018-08-07',
			'address': '5906 Ostrom Ave',
			'city': 'Encino',
			'state': 'CA',
			'zipcode': '91316'
		}
		response = self.client.post('/zlistings/', test_listing)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(len(ZListing.objects.all()), 4)


	## Test to create a new listing with missing parameters (address)
	def test_create_listing_without_required(self):
		test_listing = {
			'id': 4,
			'area_unit': 'SqFt',
			'bathrooms': 3,
			'bedrooms': 4,
			'home_size': 1470,
			'home_type': 'SingleFamily',
			'last_sold_date': '2016-03-29',
			'last_sold_price': 670000,
			'link': 'https://www.zillow.com/homedetails/5906-Ostrom-Ave-Encino-CA-91316/19977905_zpid/',
			'price': 6000,
			'property_size': 6002,
			'rent_price': '',
			'rentzestimate_amount': 3195,
			'rentzestimate_last_updated': '2018-08-07',
			'city': 'Encino',
			'state': 'CA',
			'zipcode': '91316'
		}
		response = self.client.post('/zlistings/', test_listing)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	## Test to retrieve a single listing
	def test_get_single_listing(self):
		response = self.client.get('/zlistings/1')
		self.assertRedirects(response, '/zlistings/1/', status_code=301, target_status_code=200)


	## Test to update a single listing
	def test_update_single_listing(self):
		test_listing = {
			'id': 2,
			'link': 'https://www.zillow.com/homedetails/5906-Ostrom-Ave-Encino-CA-91316/19977905_zpid/',
			'price': 6000,
			'address': '5906 Ostrom Ave',
			'city': 'Encino',
			'state': 'ON',
			'zipcode': '91316'
		}
		response = self.client.put('/zlistings/2/', test_listing)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		zlisting = ZListing.objects.get(id=2)
		self.assertEqual(zlisting.link, test_listing['link'])


	## Test to delete a single listing
	def test_delete_single_listing(self):
		response = self.client.delete('/zlistings/3/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(len(ZListing.objects.all()), 2)
