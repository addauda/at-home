from django.db import models

# Create your models here.
class Listing(models.Model):

	class HomeType(models.TextChoices):
		SINGLE_FAMILY = 'SingleFamily'
		VACANT_RESIDENTIAL_LAND = 'VacantResidentialLand'
		MISCELLANEOUS = 'Miscellaneous'
		MULTI_FAMILY = 'MultiFamily2To4'
		CONDOMINIUM = 'Condominium'
		APARTMENT = 'Apartment'
		DUPLEX = 'Duplex'

	id = models.PositiveIntegerField(primary_key=True)
	area_unit = models.CharField(max_length=10, null=True)
	bathrooms = models.FloatField(null=True)
	bedrooms = models.FloatField(null=True)
	home_size = models.FloatField(null=True)
	home_type = models.CharField(max_length=50, choices=HomeType.choices, null=True)
	last_sold_date = models.DateField(null=True)
	last_sold_price = models.FloatField(null=True)
	link = models.TextField(null=True)
	price = models.FloatField(null=True)
	property_size = models.FloatField(null=True)
	rent_price = models.FloatField(null=True)
	rentzestimate_amount = models.FloatField(null=True)
	rentzestimate_last_updated = models.DateField(null=True)
	tax_value = models.FloatField(null=True)
	tax_year = models.PositiveSmallIntegerField(null=True)
	year_built = models.PositiveSmallIntegerField(null=True)
	zestimate_amount = models.FloatField(null=True)
	zestimate_last_updated = models.DateField(null=True)
	address = models.CharField(max_length=50, null=False)
	city = models.CharField(max_length=20, null=False)
	state = models.CharField(max_length=5, null=False)
	zipcode = models.CharField(max_length=10, null=False)

	class Meta:
		ordering = ['price']
		db_table = 'listings'
