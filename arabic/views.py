from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from arabic.nlp_arabic import determine_pos

class ArabicSentence(APIView):

	def get_queryset(self):
		given_sentence = self.request.query_params.get('s')

		if given_sentence is None:
			return None
		
		return given_sentence


	def get(self, request):
		query = self.get_queryset()
		if not query:
			return Response({})

		data = determine_pos(query)
		return Response(data)

