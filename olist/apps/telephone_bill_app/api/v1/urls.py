from django.urls import path

from apps.telephone_bill_app.api.v1.bills import views as bills

urlpatterns = [
    path('bill/<int:pk>', bills.GetTelephoneBillView.as_view(), name='v1_telephone_bill'),
]
