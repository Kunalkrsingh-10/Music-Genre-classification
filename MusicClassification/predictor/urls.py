from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'predictor'

urlpatterns = [
    # change
    path('', views.Work, name='Work'),
    path('result',views.model_form_upload,name = 'result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
