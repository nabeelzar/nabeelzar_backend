# Create your views here.
from cats.models import Cat 
from cats.serializers import CatSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from random import choice


class CatObj(APIView):

	# @staticmethod
	# def pick_random_object():
	# 	try:
	# 		return random.randrange(1, Cats.objects.all().count() + 1)
	# 	except: 
	# 		return None 

	# def get_object(self):
	# 	try:
	# 		rand_id = self.pick_random_object()
	# 		print(f'{rand_id=}')
	# 		if not rand_id:
	# 			raise Http404

	# 		return Cats.objects.all().filter(id = rand_id)[0]
	# 	except Cats.DoesNotExist: 
	# 		raise Http404

	def get_object(self):
		"""Get all the pks and choose a random Cat"""
		pks =  Cat.objects.values_list('pk', flat=True).order_by('id')
		random_pk= choice(pks)
		return Cat.objects.get(pk=random_pk)


	def get(self, request, *args, **kwargs):
		try:
			cat = self.get_object()
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = CatSerializer(cat)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = CatSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
