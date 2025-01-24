from django.http import HttpResponse, JsonResponse

def home(request):
    print("Home page request")
    friends = ['Ram','shyam ', 'Hari']
    return JsonResponse(friends, safe=False)