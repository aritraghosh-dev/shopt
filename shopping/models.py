from django.db import models
#signin
class signinm(models.Model):
    name=models.CharField( max_length=100)
    email=models.EmailField(unique=True,null=False ,blank=False) 
    number=models.CharField( max_length=500)
    password1=models.CharField( max_length=500)
    adress=models.CharField( max_length=5000)
    def __str__(self):
        return self.name
#catagorymodel
class catagory(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
#product
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    decription=models.CharField(max_length=500,default='')
    image=models.ImageField(upload_to='Uploades')
    cat=models.ForeignKey(catagory,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name


    
    

