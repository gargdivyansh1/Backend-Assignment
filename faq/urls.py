from django.urls import path
from .views import FAQAPIView

urlpatterns = [
    path("faqs/", FAQAPIView.as_view(), name="faq-list"),
]
