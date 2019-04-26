# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restroapi.models import Restro
from restroapi.serializers import RestroSerializer


@csrf_exempt
def restro_list(request):
   
    if request.method == 'GET':
        restro = Restro.objects.all()
        serializer = RestroSerializer(restro, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def restro_detail(request, pk):
    """
    Retrieve, update or delete a code restro.
    """
    try:
        restro = Restro.objects.get(pk=pk)
    except Restro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestroSerializer(restro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RestroSerializer(restro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        restro.delete()
        return HttpResponse(status=204)