from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import KakaoFriend
import json
from django.core.serializers import serialize


class IndexView(View):
    def get(self, request):
        friends = KakaoFriend.objects.all().order_by('-id')
        data = json.loads(serialize('json', friends))
        return JsonResponse({'items': data})

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            friend = KakaoFriend(name = request['name'],
                                 type = request['type'],
                                 job = request['job'],
                                 age = request['age'])
        else:
            friend = KakaoFriend(name = request.POST['name'],
                                 type = request.POST['type'],
                                 job = request.POST['job'],
                                 age = request.POST['age'])
        friend.save()
        return HttpResponse(status=200)

    def put(self, request):
        request = json.loads(request.body)
        id = request['id']
        age = request['age']
        friend = get_object_or_404(KakaoFriend, pk=id)
        friend.age = age
        friend.save()
        return HttpResponse(status=200)

    def delete(self, request):
        request = json.loads(request.body)
        id = request['id']
        friend = get_object_or_404(KakaoFriend, pk=id)
        friend.delete()
        return HttpResponse(status=200)
