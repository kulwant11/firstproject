from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("welcome on home page")
    return render(request, 'student/home.html')

def about(request):
    #return HttpResponse("welcome on home page")
    return render(request, 'student/about.html')

def service(request):
    #return HttpResponse("welcome on home page")
    return render(request, 'student/service.html')

def signup(request):
    #return HttpResponse("welcome on home page")
    
    context={}
    if(request.POST):
        email=request.POST['email']
        #email=request.POST('email')
        password=request.POST['pass']

        my_list=[10,20,30,"Neetu"]
        #context={'email':email, 'password':password, 
        #'my_key':my_list}
        d={'email':email, 'password':password }
        context={'mydata':d}
    

        print("Email is>>",email)
        print("Password is>>", password)
    
    return render(request, 'student/signup.html', context)



def newregister(request): 
    #using get method
    '''if(request.GET):
        name=request.GET.get('na', '')
        email=request.GET['email']
        passw=request.GET['pass']
        sell=request.GET['sell']
        rad=request.GET['radi']
        chek=request.GET['10']
        chek1=request.GET['12']
        chek2=request.GET['ba']
        comm=request.GET['comment']

        print("name is>>",name)
        print("email is>>",email)
        print("password is>>",passw)
        print("drop down is>>",sell)
        print("Radio is>>",rad)
        print("checkbox is>>",chek)
        print("checkbox1 is>>",chek1)
        print("checkbox2 is>>",chek2)
        print("comment is>>",comm)'''
    context={}
    if(request.POST):
        name=request.POST.get('na', '')  #'' default value
        email=request.POST.get('email','')
        passw=request.POST.get('pass','')
        sell=request.POST.get('sell','')
        rad=request.POST.get('radi','')
        chek=request.POST.get('10', '')
        chek1=request.POST.get('12', '')
        chek2=request.POST.get('ba', '')
        comm=request.POST.get('comment','')


        '''my_list=[10,20, 30, 40, "Demo"]
        e={'name':name, 'password':passw}
        context={'mydata1':e}'''

        print("name is>>",name)
        print("email is>>",email)
        print("password is>>",passw)
        print("drop down is>>",sell)
        print("Radio is>>",rad)
        print("checkbox is>>",chek)
        print("checkbox1 is>>",chek1)
        print("checkbox2 is>>",chek2)
        print("comment is>>",comm)    
        
        context={'name':name, 'Email':email, 'password':passw, 'DOB':sell, 'Gender':rad,
        'checkbox':chek, 
        'checkbox1':chek1, 
        'checkbox2':chek2, 
        'comment':comm}

        '''context={'name':name, 'Email':email, 'password':passw, 'DOB':sell, 'Gender':rad,
        'checkbox':chek, 
        'checkbox1':chek1, 
        'checkbox2':chek2, 
        'comment':comm,
        'my_key':my_list }'''

        

    return render(request, 'student/newregister.html', context)



#url->view->templates

