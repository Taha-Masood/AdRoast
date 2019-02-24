from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from api.FeatureServerExtraction import *

@csrf_exempt
def analysisPOST(request):
    print('POST Request Recieved :' + request.method)
    if request.method == 'POST':
        with open("parsedImage.png", "wb") as fh:
            fh.write(base64.decodebytes(request.body))
        result = extract_feature("parsedImage.png")
        data = {
            'grade': result[0],
            'improvements': result[1],
            'score': result[2]
        }
        print('1:' + result[0])
        print('2:' + result[1][0])
        print('3:' + str(result[2]))
    else:
        data = {
            'response': 'Not a POST request'
        }
        return JsonResponse(data)
