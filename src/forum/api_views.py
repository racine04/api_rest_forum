from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from forum.models import ForumModel
from forum.serializers import ForumSerializer





@csrf_exempt
def forum_list(request):

    if request.method == "GET":
        forums = ForumModel.objects.all()
        serializer= ForumSerializer(forums, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=ForumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def forum_detail(request, pk):
    try:
        forum = ForumModel.objects.get(pk=pk)
    except ForumModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ForumSerializer(forum)
        return JsonResponse(serializer.data)