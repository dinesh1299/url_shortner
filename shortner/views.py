from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from .models import url, analytics
from datetime import datetime, timezone
from django.core.cache import cache
from utility.functions import (
    validate_url, generate_expires_at, generate_ip, generate_short_url
)
# Create your views here.


def shorten(request):
    try:
        if request.POST:
            original_url = request.POST.get("original_url")
            if not original_url or not validate_url(original_url):
                return JsonResponse({"success": False, "message": "Invalid original url"})
            short_url = generate_short_url(original_url, request)
            expires_at = generate_expires_at(int(request.POST.get("expires_in", None) or 24))
            method_name = "create"
            if url.objects.filter(original_url=original_url).exists():
                method_name = "update"
            getattr(url.objects, method_name)(original_url=original_url, shortend_url=short_url, expires_at=expires_at)
            return JsonResponse({"success": True, "message": f"Shortend url for {original_url} is {short_url}"})
        return JsonResponse({"success": False, "message": "Method not allowed"})
    except Exception as e:
        return JsonResponse({"success": False, "message": "Unexcepted exception occurred"})


def list_url(request):
    url_list = url.objects.all()
    return render(request, "list_url.html", {"url_list": url_list})


def json_url(request):
    url_list = list(url.objects.values("id", "original_url", "shortend_url"))
    return JsonResponse(url_list, safe=False)


def shorten_url(request, short_url):
    try:
        url_obj = url.objects.filter(shortend_url=f"http://{request.get_host()}/{short_url}")
        ip_address = generate_ip()
        if not url_obj.exists():
            return JsonResponse({"success": False, "message": "Invalid Short Url"})
        if url_obj.first().expires_at < datetime.now():
            return JsonResponse({"success": False, "message": "Link Expired."})
        cache_key = f"analytics:{url_obj.first().id}:{ip_address}"
        if cache.get(cache_key):
            return redirect(url_obj.first().original_url)
        analytics.objects.create(shortend_url=url_obj.first(), ip_address=ip_address)
        cache.set(cache_key, True, timeout=5)    
        return redirect(url_obj.first().original_url)
    except Exception as e:
        return HttpResponse("Error 505.")


def analytics_view(request, short_url):
    url_obj = url.objects.filter(shortend_url=f"http://{request.get_host()}/{short_url}")
    if not url_obj.exists():
        return JsonResponse({"success": False, "message": "Invalid Short Url"})
    analytics_obj = list(analytics.objects.filter(shortend_url=url_obj.first()).values())
    return JsonResponse(analytics_obj, safe=False)


def index(request):
    return render(request, "index.html")