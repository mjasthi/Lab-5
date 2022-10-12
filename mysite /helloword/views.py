
import json
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse

# Function based view
def myView(request):
    data = {
        "message": "Hello world"
    }

    return HttpResponse(json.dumps(data), content_type = "application/json")


