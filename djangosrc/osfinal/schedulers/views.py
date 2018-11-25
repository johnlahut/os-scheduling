from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .schedulers.fcfs import fcfs
from .schedulers.sjf import sjf
from .schedulers.pri import pri
# Create your views here.

# RESTful endpoints, GET only
def fcfs_api(request):
    return JsonResponse(fcfs(n=4, burst_time=[20, 15, 10, 5]))

def sjf_api(request):
    return JsonResponse(sjf(n=4, burst_time=[20, 5, 25, 10]))

def pri_api(request):
    return JsonResponse(pri(n=4, burst_time=[20, 15, 10, 5], priority=[1, 2, 3, 4]))

def sched_home(request):
    return HttpResponse("Hello world!")