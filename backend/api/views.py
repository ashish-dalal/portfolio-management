import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tools import first_page

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools/NSE"), 'r') as f:
    stocks = [line[:-1] for line in f.readlines()]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools/NIFTY50"), 'r') as f:
    nifty50 = [line[:-1] for line in f.readlines()]

@api_view(['GET'])
def search(request):
    result = [stock for stock in stocks if stock.startswith(str(request.GET.get('search', None)).upper())]
    return Response({"stocks": result}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_NIFTY_50(request):
    return Response({"stocks": nifty50}, status=status.HTTP_200_OK)