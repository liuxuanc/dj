from django.urls import path
from myproperty import views
from django.views.generic import TemplateView
from myproperty import views
from myproperty.views import LoginView, LogoutView

from django.conf.urls.static import static
from djangoProject import settings

app_name = 'myproperty'

urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('register/', views.register, name='register'),

    path('infodata/', views.infodata, name='infodata'),
    path('navigation/', views.navigation, name='navigation'),
    path('management/', views.management, name='management'),
    path('workflow/', views.workflow, name='workflow'),

    path('showdata/', views.showdata, name='showdata'),
    path('findinfo/', views.findinfo, name='findinfo'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('getlentype/', views.getlentype, name='getlentype'),
    path('selectinfo/', views.selectinfo, name='selectinfo'),
    path('selectsn/', views.selectsn, name='selectsn'),
    path('saveffbtn/', views.saveffbtn, name='saveffbtn'),
    path('selectrecover/', views.selectrecover, name='selectrecover'),
    path('savehsbtn/', views.savehsbtn, name='savehsbtn'),

    path('grantdata/', views.grantdata, name='grantdata'),
    path('showsign/', views.showsign, name='showsign'),
    path('calendar/', views.calendar, name='calendar'),



    # path('findsearch/', views.findsearch, name='findsearch'),
    # path('distribute/', views.distribute, name='distribute'),

    ]
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
