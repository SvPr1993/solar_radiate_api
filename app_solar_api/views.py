from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app_solar_api.service import random_num, random_num_2

# Метод возвращает json с рандомными числами
class Number(APIView):
    def get(self, request):
        int_num = random_num()
        int_num_2 = random_num()
        json_anwser = {"start_number": int_num, "end_number": int_num_2}
        return Response(json_anwser)

