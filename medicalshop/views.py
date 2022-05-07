from django.shortcuts import render,redirect
from medicalshop.models import Stock
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def master(request):
     return render(request,'medicalmaster.html')

def home(request):
     return render(request,'medicalhome.html')     

def add(request):
     if request.method == "POST":
          name=request.POST['medicine']
          per=request.POST['per']
          quan=request.POST['quantity']
          sell=request.POST['sellcost']
          stk=Stock(medicine_name=name,medicine_per=per, medicine_qunatity=quan, medicine_sellingprice=sell )
          stk.save()
          return redirect('/medical/addproduct')



def addproduct(request):
     viewstock=Stock.objects.all()
     print(viewstock)
     return render(request,'addproduct.html',{'viewstock':viewstock})


@csrf_exempt
def search_list(request):
    if request.method=='POST':
        searchlist=request.POST['search']
        if searchlist!="":
            srch_products=Stock.objects.filter(Q(medicine_name__icontains=searchlist) )
            print(srch_products)
            if srch_products.exists():
                return render(request,'search.html',{'searchproduct':srch_products})
            else:
                return render(request,'bill.html',{'msg':' No Result Found '}) 
        else:
            return redirect('/medical/bill')    
    else:
        return redirect('/medical/bill')   
             

def search(request):
     
     return render(request,'search.html') 

@csrf_exempt       
def update(request):
     quan=int(request.POST['quantity'])
     stockid=request.POST['stockid']
     print(quan,stockid)
     obj=Stock.objects.get(id=stockid)
     print(obj)
     obj.medicine_qunatity-quan
     obj.medicine_qunatity=obj.medicine_qunatity-quan
     obj.save()
     return JsonResponse({'msg':'Updated Successfully'}) 
     


def bill(request):
     
     return render(request,'bill.html')  


def Purchase(request):
     purchacestock=Stock.objects.filter(medicine_qunatity__lte=5)
     return render(request,'Purchace.html',{'purchacestock':purchacestock}) 

def billgenerate(request):
     return render(request,'billgenerate.html')                     