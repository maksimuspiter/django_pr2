from django.shortcuts import render, HttpResponse

def hello_world(request):
    return HttpResponse(f'Hello {request.user.username}')