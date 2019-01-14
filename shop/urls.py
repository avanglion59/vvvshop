from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .views import index, detail, goods

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:item_id>/', detail, name='detail'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('goods', goods, name='goods')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
