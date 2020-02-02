from rest_framework import generics
from .models import ZListing
from .serializers import ZListingSerializer

class ZListingList(generics.ListCreateAPIView):
	queryset = ZListing.objects.all()
	serializer_class = ZListingSerializer

class ZListingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ZListing.objects.all()
	serializer_class = ZListingSerializer
