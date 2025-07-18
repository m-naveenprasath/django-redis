import time
from django.http import JsonResponse
from django.core.cache import cache

def no_cache_view(request):
    time.sleep(3)  # Simulate slow operation
    return JsonResponse({'data': 'Response without cache'})

def with_cache_view(request):
    result = cache.get('my_cached_key')
    if not result:
        time.sleep(3)  # Simulate same slow operation
        result = 'Response with Redis cache'
        cache.set('my_cached_key', result, timeout=60)
    return JsonResponse({'data': result})
