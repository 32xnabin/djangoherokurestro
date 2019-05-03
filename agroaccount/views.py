from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from agroaccount.models import Agro
from agroaccount.serializers import AgroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



class AgroView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        if request.method == 'GET':
            agro = Agro.objects.all()
            serializer = AgroSerializer(agro, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AgroSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


    # @csrf_exempt
    # def agro_list(request):
    
    #     if request.method == 'GET':
    #         agro = Agro.objects.all()
    #         serializer = AgroSerializer(agro, many=True)
    #         return JsonResponse(serializer.data, safe=False)

    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = AgroSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)

    # @csrf_exempt
    # def agro_detail(request, pk):
    #     """
    #     Retrieve, update or delete a code agro.
    #     """
    #     try:
    #         agro = Agro.objects.get(pk=pk)
    #     except Agro.DoesNotExist:
    #         return HttpResponse(status=404)

    #     if request.method == 'GET':
    #         serializer = AgroSerializer(agro)
    #         return JsonResponse(serializer.data)

    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = AgroSerializer(agro, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)

    #     elif request.method == 'DELETE':
    #         agro.delete()
    #         return HttpResponse(status=204)
