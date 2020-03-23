
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginPage, name ='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.logoutView, name='logout'),
    url(r'^document_list/', views.document_list, name ='document_list'),
    url(r'^buttons/', views.buttons),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^history/', views.history),
    url(r'^register/', views.registerPage, name='register'),


]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)