from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('events/', views.events, name="events"),
    path('events/<int:pk>/', views.eventspecific, name="eventspecific"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:pk>/', views.blogspecific, name="blogspecifoc"),
    path('contact/', views.contact, name="contact"),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)