from django.http import JsonResponse

# Create your views here.
def home(request):
    data={
        'message':'welcome to the ecommerce store web !'
    }
    return JsonResponse(data)