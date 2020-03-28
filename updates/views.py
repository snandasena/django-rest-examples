from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
import json
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize


# Create your views here.

# def details_view(request):
#     return HttpResponse(get_template)


def update_model_details_view(request):
    data = {
        "name": "Django",
        "content": "Great"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type="application/json")


class JsonCBV(View):
    def get(self, request, *args, **keywords):
        data = {
            "name": "Django",
            "content": "Great"
        }
        json_data = json.dumps(data)
        # return JsonResponse(data)
        return HttpResponse(json_data, content_type="application/json")


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **keywords):
        data = {
            "name": "Django",
            "content": "Great"
        }
        return self.render_to_json_response(data)


class SerializedView(View):
    def get(self, request, *args, **keywords):
        obj = Update.objects.get(id=1)
        data = {
            "name": obj.user.name,
            "content": obj.user.content
        }
        json_data = json.dumps(data)
        # return JsonResponse(data)
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *args, **keywords):
        qs = Update.objects.all()

        data = serialize("json", qs, fields=("user", "content"))
        # print(data)
        # data = {
        #     "name": "test",
        #     "content": "tewsrsfdsfs"
        # }
        json_data = json.dumps(data)
        # return JsonResponse(data)
        return HttpResponse(data, content_type="application/json")
