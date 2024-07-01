
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('gallery/', views.Gallery,name='gallery'),
    path('about/',views.about),
    path('services/',views.services),
    path('info/',views.info,name='info'),
    path('homework/',views.homework),
    path('form/',views.form,name='form'),

]
