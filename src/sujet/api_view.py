from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import SujetModel
from forum.models import ForumModel
from .serializers import SujetSerializer


@csrf_exempt
def sujet_list(request, forum_id):
    if request.method == 'GET':

        subjects = SujetModel.objects.filter(forum=forum_id)
        serializer = SujetSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SujetSerializer(data=data)
        forum = ForumModel.objects.get(id=forum_id)
        if serializer.is_valid():
            serializer.save(forum=forum)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def sujet_detail(request, pk):
    try:
        subject = SujetModel.objects.get(pk=pk)
    except SujetModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SujetSerializer(subject)
        return JsonResponse(serializer.data)
