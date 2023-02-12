from django.shortcuts import render
#import openpyxl

import csv
import pandas

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import IAP

# # Load the workbook
# workbook = openpyxl.load_workbook('iap_requirements.xlsx')

# # Select the sheet you want to read
# sheet = workbook['Sheet1']

# # Iterate over the rows and columns of the sheet
# for row in sheet.iter_rows():
#     for cell in row:
#         print(cell.value)

# # You can also access a specific cell value using its coordinates
# cell_value = sheet.cell(row=1, column=1).value
# print(cell_value)


#Serializer 
class ProductSerialiser(serializers.ModelSerializer):

    class Meta:
        model = IAP
        fields = "__all__"


#viewset

class ProductViewSet(viewsets.ModelViewSet):
    queryset = IAP.objects.all()
    serializer_class = ProductSerialiser

    @action(detail=False, methods=['POST'])
    def Upload_data(self, request):
        file = request.FILES["file"]
        excel = pandas.read_excel(file)
        IAP_list = [
                IAP(
                site_id = df['site_id'],
                site_name = df['site_name'],
                country = df['country'],
                order_id = df['order_id'],
                purchase_id = df['purchase_id'],
                csm_id = df['csm_id'],
                serial = df['serial'].lower(),
                ip_address = df['ip_address'],
                model = df['model'],
                macaddr = ':'.join(df['macaddr'][i:i+2] for i in range(0,12,2))
                )
                for i, df in excel.iterrows()
        ]

        IAP.object.bulk_create(IAP_list)

        return Response("SUCCESSFULLY UPLOADED THE DATA")