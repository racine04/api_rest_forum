from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from message.models import MessageModel
from message.serializers import MessageSerializer
from sujet.models import SujetModel



@csrf_exempt
def message_list(request,sujet_id):

    if request.method == 'GET':
        messages = MessageModel.objects.filter(subject=sujet_id)
        serializer = MessageSerializer(messages, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        subject = get_object_or_404(SujetModel, id = sujet_id)
        if serializer.is_valid():
            serializer.save(subject=subject)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

