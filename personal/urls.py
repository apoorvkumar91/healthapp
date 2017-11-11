from django.conf.urls import url #specify url patterns
from . import views # . implies we are importing from current package

urlpatterns = [
        url(r'^$', views.index, name="index")]