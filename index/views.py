from django.shortcuts import render

from commodity.models import *


# Create your views here.
def indexView(request):
    title = "首頁"
    classContent= ''
    commodityInfo = CommodityInfo.objects.order_by('-sold').all()[:8]

    types = Type.objects.all()
