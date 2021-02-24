from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GrocerySerializer
from .models import Grocery

def post_list(request):
    posts = Grocery.objects.all().order_by('price')
    return render(request, 'groceries/post_list.html', {'posts': posts})

class GroceryList(APIView):
    def get(self,request):
        GroceryList=Grocery.objects.all()
        serializer=GrocerySerializer(GroceryList,many=True)
        return Response(serializer.data)



    def post(self):
        pass
