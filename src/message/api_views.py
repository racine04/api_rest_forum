from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import MessageModel
from .serializers import MessageSerializer
from sujet.models import SujetModel


@csrf_exempt
def message_list(request, subject_id):

    try:
        subject = SujetModel.objects.get(pk=subject_id)
    except SujetModel.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        messages = MessageModel.objects.filter(subject=subject.id)
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        subject = get_object_or_404(SujetModel, id=subject.id)
        if serializer.is_valid():
            serializer.save(subject=subject)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
