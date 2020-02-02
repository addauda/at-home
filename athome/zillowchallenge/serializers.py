from rest_framework import serializers
from .models import ZListing

class ZListingSerializer(serializers.ModelSerializer):

	class Meta:
		model = ZListing
		fields = '__all__'
