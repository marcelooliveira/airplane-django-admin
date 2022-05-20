from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from custom.models import Category, Product, Inventory

def index(request):
  inventories = Inventory.objects.select_related('product').order_by('product')
  template = loader.get_template('report.html')
  context = {
      'inventories': inventories
  }
  return HttpResponse(template.render(context, request))
