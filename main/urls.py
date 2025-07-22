from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path("About/",views.About,name="About"),
    path("blog/", views.blog, name="blog"),
    path("portfolio/", views.portfolio, name="portfolio"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
