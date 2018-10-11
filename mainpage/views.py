from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import StudentModel
from django.views.generic import View
from pymongo import MongoClient
import time


def index(request):
    return HttpResponse("Hello,world. You are at the poll index")


class Student(View):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['WeatherData']
        self.collection = self.db['WeatherData']

    # def get(self, request):
    #     StudentModel.objects.create(name='水痕', age= 20)
        # result = StudentModel.objects.filter().count()
        # return HttpResponse('create')
        # return  HttpResponse(result)

    def get(self, request):
        outprint = 'By %s, you got %i datas.' % (time.strftime('%X %x %Z'), self.collection.find().count())
        return HttpResponse(outprint)
        #

    def update(self, request):
        result = StudentModel.objects.filter(name='水痕').first().update(name='张三')
        print(result)
        return HttpResponse('hello word')
