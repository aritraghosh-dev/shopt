import re 
from shopping.models import signinm
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email): 
    if(re.search(regex,email)):  
        return True  
    else:  
        return False 
def signs(a):
    if signinm.objects.filter(email=a.get('Email1')).count() ==0:
        signinm(name=a.get("name"),email=a.get('Email1'),number=a.get('Number'),password1=a.get('password1'),adress=a.get('address')).save()
        return True
    else:
        return False
def charcount(word,k):
    j=0
    for i in word :
        j+=1
    if j>k :
        return True
    else:
        return False

# def loginva(request):
#     email=request.POST.get('Email1')
#     password1=request.POST.get('password1')
#     a=signinm.objects.filter(email=email)
#     if password1==a[0].password1 :
#         return True
#     else:
#         if a.count()==0:
#             message="please sign in."
#         else:
#             message="invalid Password"
def contva(request):
    email=request.POST.get('Email1')
    password1=request.POST.get('password1')
    a=signinm.objects.filter(email=email)
    if password1==a[0].password1 :
        print("Done")
    

def signva(request):
    name=request.POST.get('name')
    email=check(request.POST.get('Email1'))
    number=request.POST.get('Number')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')
    adress=request.POST.get('address')
    password= password1==password2
    if email and password and charcount(name,2) and charcount(adress,4) and charcount(number,8):
        if signs(request.POST) :
            message=False
        else:
            message=["Already Have an account"]
        return message
    else :
        message = []
        if email is False:
            message.append(" Invalid Email")
        if charcount(name,2) is False:
            message.append("The name is too short.")
        if charcount(adress,4) is False:
            message.append("The Adress is too short.")
        if charcount(number,8) is False:
            message.append("The Number  is too short.")
        if password is False:
            message.append("BOTH PASSWORD SHOULD BE SAME, ")
        return message

