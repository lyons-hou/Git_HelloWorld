from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from BiosUpload.models import BIOS_Package
from BusinessGroup.models import BusinessGroup_Info 
from ProductInfo.models import ProductFamily
from ProductInfo.models import ProductInfo
# Create your views here.

#class BiosListForm(forms.Form):
#   BU = forms.ModelChoiceField(BusinessGroup_Info.objects.all(), label='BusinessGroup')
#   Family = forms.ModelChoiceField(ProductFamily.objects.all(), label='Family')
#   Product = ProductInfo.objects.all().order_by('id')

#class BiosResultForm(request):
#   BiosPackage = BIOS_Package.objects.filter(Product=request.GET.get(
   
def BiosList(request):
   if request.method == 'GET':
       BU = BusinessGroup_Info.objects.all().order_by('id')
       try: 
          BU_URL = int(request.GET.get("BU"))
       except:
          BU_URL = BU[0].id 

       Family = ProductInfo.objects.filter(Business_Group_id=BU_URL).distinct('Product_Family_id')
       try:
          Family_URL = int(request.GET.get("Family"))
       except:
          Family_URL = Family[0].Product_Family_id 

       Product = ProductInfo.objects.filter(Product_Family_id=Family_URL).distinct('ProductName')
       try:
          Product_URL = request.GET.get("Product")
       except:
          Product_URL = Product[0].ProductName

       if BU_URL == 6:
           Customer = BIOS_Package.objects.filter(ProductName=Product_URL,id=BU_URL).distinct('CustomerName') | BIOS_Package.objects.filter(ProductName=Product_URL,id=BU_URL).distinct('CustomerName') | BIOS_Package.objects.filter(ProductName=Product_URL,id=BU_URL).distinct('CustomerName')
       else:          
           Customer = BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='PKG').distinct('CustomerName') | BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='PKG_FULL').distinct('CustomerName') | BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='CAB').distinct('CustomerName')
       try:
          Customer_URL = request.GET.get("Customer")
       except:
          Customer_URL = Customer[0].CustomerName

       if BU_URL == 6:
           BiosList = BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='OTHER').order_by('-Version') 
       else:
           if Customer_URL == '0':
               BiosList = BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='PKG').order_by('-Version') | BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='PKG_FULL').order_by('-Version') | BIOS_Package.objects.filter(ProductName=Product_URL,PackageType='CAB').order_by('-Version')
           else:
               BiosList = BIOS_Package.objects.filter(ProductName=Product_URL,CustomerName=Customer_URL,PackageType='PKG').order_by('-Version') |  BIOS_Package.objects.filter(ProductName=Product_URL,CustomerName=Customer_URL,PackageType='PKG_FULL').order_by('-Version') | BIOS_Package.objects.filter(ProductName=Product_URL,CustomerName=Customer_URL,PackageType='CAB').order_by('-Version')

   else: 
       BU = BusinessGroup_Info.objects.all().order_by('Business_Group')
       Family = ProductInfo.objects.filter(Business_Group_id=BU[0].id)
       Product = ProductInfo.objects.all().order_by('id')

   return render(request, 'BiosList.html',locals())
