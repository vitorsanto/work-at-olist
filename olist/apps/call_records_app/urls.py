from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.call_records_app.api.v1.urls')),
]
