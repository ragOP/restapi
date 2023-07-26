from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home ")
    array=['rag,naj,sam','red','green']


    return JsonResponse(array,safe=False)