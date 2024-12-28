import time
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

def index(request):
    # print("HELLO I'm not using cache")
    ans = compute_heavy_list(invalidate=False)
    return HttpResponse(f"{ans}")

def invalidate(request):
    ans = compute_heavy_list(invalidate=True)
    return HttpResponse(f"{ans}")

def compute_heavy_list(invalidate = False):
    CACHE_KEY = 'cache_numbers'
    INITIAL_CACHE_VALUE = [1,2,3,4,5]
    cached_value = cache.get(CACHE_KEY)
    if cached_value is None : 
        cache.set(CACHE_KEY, INITIAL_CACHE_VALUE)
        return INITIAL_CACHE_VALUE
    if invalidate  : 
        print("Computing for 5 seocnds")
        time.sleep(5)
        CACHE_VALUE = [9,9,9]
        print(f"Set {CACHE_KEY} with {CACHE_VALUE} ")
        cache.set(CACHE_KEY,CACHE_VALUE)
        return CACHE_VALUE
    else :
        print(f"RETRIEVING CACHE_VALUE {cached_value}")
        return cached_value

        