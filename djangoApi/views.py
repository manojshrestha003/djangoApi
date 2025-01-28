from django.http import HttpResponse, JsonResponse

def home(request):
    
    friends = ['Ram','shyam ', 'Hari']
    return JsonResponse(friends, safe=False)