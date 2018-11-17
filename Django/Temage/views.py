from django.shortcuts import render
from Temage.models import User
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

# Create your views here.
def get_user(request, num):
    
    user = User.objects.get(id=int(num))
    json_data = serializers.serialize('json', [user,])
    json_data = json.loads(json_data)
    result = json.dumps(json_data[0]).replace('\"',"\'")
    return HttpResponse(json.dumps(result), content_type="application/json")
