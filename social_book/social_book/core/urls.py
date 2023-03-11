from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('settings', views.settings, name='settings'),
                  path('upload', views.upload, name='upload'),
                  path('signup', views.signup, name='signup'),
                  path('signin', views.signin, name='signin'),
                  path('logout', views.logout, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
