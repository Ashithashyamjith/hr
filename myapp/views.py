from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'index.html')
def test1(request):
    return render(request,'main.html')
def test2(request):
    return render(request,'home.html')
def test3(request):
    return render(request,'admin-login.html')
def test4(request):
    return render(request,'user-login.html')
def test5(request):
    return render(request,'hr-home1.html')
def test6(request):
    return render(request,'emp-reg1.html')
def test7(request):
    return render(request,'reg.html')
def test8(request):
    return render(request,'add-dept.html')
def test9(request):
    return render(request,'emp-home.html')  
def test10(request):
    return render(request,'apply-leave.html')
def test11(request):
    return render(request,'recruitment-post.html') 
def test12(request):
    return render(request,'interview.html')    
  
