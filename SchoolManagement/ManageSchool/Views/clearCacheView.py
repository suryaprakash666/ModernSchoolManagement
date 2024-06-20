from django.core.cache import cache
from django.http import HttpResponse


def clear_cache_view(request):
    cache.clear()
    return HttpResponse("Cache cleared")
