import re
from django.shortcuts import render,redirect
from adminapp.models import Question, Registration,Exam
from adminapp.views import questions
from user.models import Addproduct, Signup,ApiUsers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import Apiuserserializers 
from rest_framework.parsers import JSONParser
from django.db.models import Q
# Create your views here.



def home(req):
    if req.method =="POST":
        email=req.POST['uemail']
        paswd=req.POST['upaswd']
        change=Signup.objects.filter(id=req.session['userid']).update(email=email,paswd=paswd)
        return redirect('/user/uhome')
    else:
        id=req.session['userid']
        details=Signup.objects.get(id=id)
        return render(req,'home.html',{'details':details})

def signup(req):
    if req.method =="POST":
        fname=req.POST['fname']
        lname=req.POST['lname']
        phone=req.POST['phone']
        email=req.POST['email']
        paswd=req.POST['paswd']
        country=req.POST['country']
        u_data=Signup(fname=fname,lname=lname,phone=phone,email=email,paswd=paswd,country=country)
        u_data.save()
        return render(req,'signup.html',{'status':"successfully registered"})
    else:
        return render(req,'signup.html')

def login(req):
    if req.method =='POST':
        username=req.POST['l_email']
        paswd=req.POST['l_pass']
        try:
            l_data=Signup.objects.get(email=username,paswd=paswd)
            req.session['userid']=l_data.id
            print(l_data)
            return redirect('/user/uhome')
        except Signup.DoesNotExist:
            return render(req,'login.html',{'error':'invalid user details'})
    else:
        return render(req,'login.html')



def logout(req):
    del req.session['userid']
    return redirect('/user/login')

def view(req):
    if req.method=='POST':
        userid=req.session['userid']
        pname=req.POST['prodctname']
        pquan=req.POST['quantity']
        price=req.POST['price']
        img=req.FILES['upload']
        product=Addproduct(poductname=pname,quantity=pquan,price=price,img=img,user_id=userid)
        product.save()
        return render(req,'addpro.html',{'status':1})
    else:
        return render(req,'addpro.html',{'status':0})
    
def display(req):
    product=Addproduct.objects.filter(user_id=req.session['userid'])
    return render(req, 'displaypro.html',{'product':product})

@api_view(['GET','POST'])
def api(req):
    if req.method =='POST':
        # user=req.data['username']
        # pasw=req.data['password']
        # object=ApiUsers(username=user,password=pasw)
        # object.save()

        # data=req.data
        request = JSONParser().parse(req)
        userserializer =Apiuserserializers(data=request)
        if userserializer.is_valid():
            userserializer.save()
        else:
            return Response({'status':'invalid user'})      

        return Response({'status':'data inserted'})
    else:
        user=ApiUsers.objects.all()

    # method 1
    
        # userlist=[]
        # for i in user:
        #     userlist.append({'username':i.username,'password':i.password})
        # print(userlist)

    # method 2
        userlist=Apiuserserializers(user,many=True)
        return Response({'userdetails':userlist.data})


@csrf_exempt
def checkexist(request):
    print('worked')
    check_name = request.POST['checkname']
    object = Signup.objects.filter(fname=check_name).exists()
    print(object)
    print(check_name)
    return JsonResponse({'IsExist':object})       
    

@csrf_exempt
def ajax(request):
    firstname = request.POST['addfirstname']
    lastname = request.POST['addlasttname']
    phone = request.POST['addphone']
    email = request.POST['addemail']
    password = request.POST['addpassword']
    obj = Signup(fname=firstname, lname=lastname, email=email, phone=phone, paswd=password)
    obj.save()
    return JsonResponse({'msg':'data inserted sucess'})


def ajaxhtml(req):
    return render(req,'ajaxaddproduct.html')   



def examhome(req):
    # print(exam_name)
    user = Registration.objects.all()
    obj = Exam.objects.all()
    # print(obj.title)
    return render(req,'examhome.html',{'user': user,'obj':obj})     

@csrf_exempt
def exam(request,exam_name,stu_id):
    det= Registration.objects.get(id=stu_id)
    ques=Question.objects.filter(Q(title_name__icontains=exam_name) )
    return render(request,'exam.html',{'ques': ques,'det':det})


@csrf_exempt
def viewanswer(request):
    answers = request.POST['answers']
    orginal = request.POST['orginal']
    id = request.POST['id']
    obj=Question.objects.get(id=id)

    print(answers,orginal)
    if (answers == orginal):
        mark=obj.mark
        return JsonResponse({'msg':'Correct Answer','mark':mark})
    else:
        return JsonResponse({'msg':'Wrong Answer'})    
        

    