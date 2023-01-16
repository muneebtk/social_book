from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializer import BookSerializer, Books
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


meta = MetaData()


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def all_books(request):
    books = Books.objects.filter(user=request.user)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

