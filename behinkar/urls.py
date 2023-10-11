from django.urls import path
from behinkar.views import GETAPI,mixinsAPI,alldata,mixinsAPIVIEW

urlpatterns = [
    path('getdata/',GETAPI.as_view()),
    path('all_dta/',alldata),
    path('post_data/',alldata),
    path('mixins/', mixinsAPI.as_view()),
    path('mixins/<pk>', mixinsAPIVIEW.as_view()),
]
