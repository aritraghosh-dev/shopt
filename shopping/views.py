from django.shortcuts import render,redirect
from shopping.models import *
from django.views import View
from shopping.vailid import *
from datetime import datetime
from django.urls import reverse
class homev(View):
	def get(self,request):
		# print(len(request.session.items()))
		# if request.session.get("customername")==None:
		# 	request.session["customername"]="Unknown"
		if len(request.session.items())==0:
		# 	request.session["customermail"]==None 
		# if request.session["customermail"]==None :
			messageb="HELLO FRIEND , "
			messagel="WELCOME TO ARTSHOP"
			# request.session["requestc"]="2"
			logt=False
			logd=[]
		else:
			if request.session["requestc"]=="1" :
				messageb="Hello, Welcome "
				messagel=request.session["customername"]
				request.session["requestc"]="2"
				logt=True
				logd=[request.session["customername"]]
			# elif request.session["customername"]!=None:
			# 	logt=True
			else:
				messageb=False
				messagel=request.session["customername"]
				logt=True
				logd=[request.session["customername"]]
				logid=request.session["customerid"]
		c={	'messageb':messageb,
			'messagel':messagel,
			'b':product.objects.all(),
			'catagory':catagory.objects.all(),
			"logt":logt,
			"logd":logd,}
		# else:
		# 	c={	'messageb':'HEY FRIEND! ',
		# 	'messagel':request.session.get("customername"),
		# 	'b':product.objects.all(),
		# 	'catagory':catagory.objects.all(),}
		return render(request,'home.html',c)

# def cartv(request):
# 	return render(request,'cart.html')

def logout(request):
	request.session.flush()
	return redirect('home')
class contractv(View):
	def get(self,request):
		return render(request,'contract.html')
	def post(self,request):
		print(request.POST)
		print(request.FILE)
		return redirect('home')

class loginv(View):
	def get(self,request):
            try :
                message=request.session["message"]
                request.session.flush()
                return render(request,'login.html',{"message":message})
            except :
                return render(request,'login.html')
		
	def post(self,request):
		email=request.POST.get('Email1')
		password1=request.POST.get('password1')
		a=signinm.objects.filter(email=email)
		if password1==a[0].password1 :
			request.session["customername"]=a[0].name
			request.session["customermail"]=a[0].email
			request.session["customerid"]=a[0].pk
			request.session["requestc"]="1"

			return redirect('home')
		else:
			if a.count()==0:
				message="please sign in."
			else:
				message="invalid Password"
			return render(request,'login.html',{"message":message})

class buyv(View):
    def get(self,request,productid):
        if len(request.session.items())==0:
            request.session["message"]=["Please login or Signin First"]
            return redirect('signin')
        else : 
            print("product purchased")
            order(
                Order_id=int(datetime.now().strftime("%d%m%y%M")+datetime.now().strftime("%H%M%S")),
                product_id=product.objects.get(pk=productid),
                price=product.objects.get(pk=productid).price,
                customer_id=signinm.objects.get(pk=request.session["customerid"]),
                email_id=request.session["customermail"],
                In_cart=False,
                ).save()
            return redirect('home')

# def cartv(request):
# 	return render(request,'cart.html')
class profile(View):
    def get(self,request):
        a=signinm.objects.get(pk=request.session["customerid"])
        return render(request,'profile.html',{"a":a})
class cartv(View):
    
    def get(self,request):
        a=order.objects.filter(email_id=request.session["customermail"],In_cart=True)
        return render(request,'cart.html',{"a":a,"i":a.count()})
class cartav(View):      
    def get(self,request,productid):
        print(productid, request)
        order(
                Order_id=int(datetime.now().strftime("%d%m%y%M")+datetime.now().strftime("%H%M%S")),
                product_id=product.objects.get(pk=productid),
                price=product.objects.get(pk=productid).price,
                customer_id=signinm.objects.get(pk=request.session["customerid"]),
                email_id=request.session["customermail"],
                In_cart=True,
                ).save()
        return redirect("home")


class signinv(View):
	def get(self,request):
            try :
                message=request.session["message"]
                request.session.flush()
                return render(request,'signin.html',{"message":message})
            except :
            
                return render(request,'signin.html')
	def post(self,request):
		name=request.POST.get('name')
		email=check(request.POST.get('Email1'))
		number=request.POST.get('Number')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		adress=request.POST.get('address')
		password= password1==password2
		a=request.POST
		if email and password and charcount(name,2) and charcount(adress,4) and charcount(number,8):
			if signinm.objects.filter(email=a.get('Email1')).count() ==0:
				b=signinm(name=a.get("name"),email=a.get('Email1'),number=a.get('Number'),password1=a.get('password1'),adress=a.get('address'))
				b.save()
				request.session["customername"]=b.name
				request.session["customermail"]=b.email
				request.session["customerid"]=b.pk
				request.session["requestc"]="1"
				return redirect('home')
			else:
				message=["Already Have an account"]
				return render(request,'signin.html',{'message':message})
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
			return render(request,'signin.html',{'message':message})

def productv(request,catagoryu):
	d=product.objects.filter(cat=catagory.objects.filter(name=catagoryu).get().pk)
	message= False
	if  d is None :
		message='No Product available'
	c={	'messageb':message,
		'b':product.objects.filter(cat=catagory.objects.filter(name=catagoryu).get().pk),
		'catagory':catagory.objects.all(),
		}
	return render(request,'products.html',c)


class orderv(View):
	def get(self,request):
            a=order.objects.filter(email_id=request.session["customermail"],In_cart=False)
            print(a.count())
            return render( request , 'order.html',{"a":a,"i":a.count()})
	def post(self,request):
		pass

# def footerv(request):
# 	return render(request,'footer.html')
# def headingv(request):
# 	return render(request,'heading.html')
# def indexv(request):
# 	return render(request,'index.html')
# def navv(request):
# 	return render(request,'nav.html',{'b':product.objects.all()})
# def productsv(request):
# 	return render(request,'products.html',{'b':product.objects.all()})

