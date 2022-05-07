from django.shortcuts import render, redirect
from adminapp.models import Exam, Question, Registration

from user.models import Signup


# Create your views here.



def dashbord(req):
    users=Signup.objects.all()
    return render(req,'dash.html',{'users':users})

def login(request):
    if request.method == "POST":
        name=request.POST['username']
        passw=request.POST['password']
        if(name == "admin" and passw == '12345'):
            return render(request,'adminhome.html') 
        else:
            try:
                deatils=Registration.objects.get(username=name,password=passw)
                request.session['userid']=deatils.id
                return redirect ('/user/examhome')
            except Registration.DoesNotExist:
                return render(request,'examlogin.html')
    return render(request,'examlogin.html')            
            #  try:
            #     worklogin=Registration.objects.get(username=name,password=passw)
            #     request.session['userid']=worklogin.id
            #     return redirect ('/user/examhome')
            # except Registration.DoesNotExist: 
            #     return render(request,'home.html')   

            


    #         deatils=Registration.objects.get(username=name,password=passw)
    #         request.session['userid']=deatils.id
    #         return redirect ('/user/examhome')
    # return render(request,'examlogin.html') 

def home(req):
    return render(req,'adminhome.html')    

def addstudent(request):
    if request.method == "POST":
        print('hi')
        studentname=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        data=Registration(name=studentname, username=username, password=password)
        data.save()
        return render(request,'addstudent.html',{'status':1}) 
    else:
        return render(request,'addstudent.html',{'status':0})    


def createexam(request):
    if request.method == "POST":
        title=request.POST['title']
        title_subject = Exam(title=title)
        title_subject.save()
        return redirect ('/admin/questions')
    return render(request,'createexam.html')       


def questions(request):
    obj = Exam.objects.all()
    if request.method == "POST":
        select=request.POST['select']
        print(select)
        question=request.POST['question']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        option4=request.POST['option4']
        mark=request.POST['mark']
        answer=request.POST['answer']
        # id=request.session['userid']
        # det= Registration.objects.get(id=id)
        # print(det)
        que= Question( title_name=select,question=question,  option1=option1,option2=option2, option3=option3, option4=option4, mark=mark, answer=answer )
        que.save()
    return render(request,'questions.html',{'obj':obj})       


def master(request):
     return render(request,'master.html')   