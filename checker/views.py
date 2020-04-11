from django.shortcuts import render
from django.shortcuts import Http404
from .models import UrlChecker


def url_checker(request):
    if not request.user.is_authenticated:
        return Http404
    all_urls_for_check = UrlChecker.objects.all()
    return render(request, 'url_checker.html', {'all_urls_for_check': all_urls_for_check})
