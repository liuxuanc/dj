from django.urls import path
from myproperty import views

from django.conf.urls.static import static
from djangoProject import settings

app_name = 'myproperty'

urlpatterns = [
    path('', views.index, name='index'),
    path('infodata/', views.infodata),
    path('navigation/', views.navigation, name='navigation'),
    path('management/', views.management, name='management'),




    path('showdata/', views.showdata, name='showdata'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('addinfo/', views.addinfo, name='addinfo'),

    ]
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
