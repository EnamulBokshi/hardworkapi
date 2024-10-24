from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render

def index (request):
    return render(request,'index.html')

# index = never_cache(TemplateView.as_view(template_name = 'index.html'))