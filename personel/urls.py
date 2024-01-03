from django.urls import path
from personel import views
urlpatterns = [
        
        path('',views.index),
        path('details/',views.details),
        path('portfolio/',views.portfolio),
        # path('login/',views.login),

]