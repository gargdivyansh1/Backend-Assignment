from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from .models import FAQ
from rest_framework import status
from .serializers import FAQSerializer
from django.http import JsonResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the FAQ API</h1><p>Use /api/faqs/ to get data.</p>")


class FAQAPIView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()
        
        faq_list = []
        for faq in faqs:
            question, answer = faq.get_translated(lang)
            faq_list.append({
                "question": question,
                "answer": answer
            })

        return Response(faq_list, status=status.HTTP_200_OK)
