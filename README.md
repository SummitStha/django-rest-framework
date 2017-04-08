# django-rest-framework
This is a simple example of Django REST framework.
Django REST framework is a powerful and flexible toolkit for building Web APIs.


# Requirements
  Python (2.7, 3.2, 3.3, 3.4, 3.5)
  
  Django (1.8, 1.9, 1.10)


# Installation
 Install using pip...
  
  pip install djangorestframework
   
 Then Add 'rest_framework' to your INSTALLED_APPS setting.
  
  INSTALLED_APPS = (
    ...
    'rest_framework',
    )
 
 
 # Finally add the followings to the project's root urls.py module:
 
  from rest_framework import routers 
  
  from core import views
  
  router = routers.DefaultRouter() 
  
  router.register(r'event', views.EventApiView)
  
  urlpatterns = [ 
    
    ... 
    
    url(r'^api/0.1/', include(router.urls))
  
  ]
      
