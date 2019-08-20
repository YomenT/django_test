from django.shortcuts import render
from django.http import HttpResponse
import uuid

# Create your views here.

def test(request, *args, **kwargs):
	var_1 = uuid.uuid4().hex[:6].upper()
	return HttpResponse("<h1>Hello World!</h1>")
