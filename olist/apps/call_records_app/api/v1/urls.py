from django.urls import path

from apps.call_records_app.api.v1.calls import views as call_record

urlpatterns = [
    path('callrecord/', call_record.CreateCallRecordView.as_view(), name='v1_create_call'),
]
