
from django.urls import path
from shopping.views import *
from project4 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', homev.as_view(), name='home'),
    path('user/<name>', homev.as_view(), name='user'),
    path('logout/', logout, name='logout'),
    path('products/<catagoryu>/', productv, name='productl'),
    path('mycart/',cartv.as_view(), name='cart'),
    path('contract/', contractv.as_view(), name='contract'),
    path('buy/12345<productid>/', buyv.as_view(), name='buy'),
    path('addcart/123465<productid>/', cartav.as_view(), name='carta'),
     path('profile/', profile.as_view(), name='profile'),
    path('login/', loginv.as_view(), name='login'),
    path('signin/', signinv.as_view(), name='signin'),
    path('order/',orderv.as_view(),name='order'),
    # path('footer/',footerv,name='footer'),
    # path('index/',indexv,name='index'),
    # path('product',productv,name='product' ),
    # path('nav/',navv,name='nav'),
    # path('products/',productsv,name='product'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
