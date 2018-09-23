from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.telephone_bill_app.api.v1.urls')),
]
