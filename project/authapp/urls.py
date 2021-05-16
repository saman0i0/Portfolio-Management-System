from django.urls import path
from .views import signin, signup, signout,addStockSubmission


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('addstock/addstocksubmission/', addStockSubmission,name='addstocksubmission')
   
]