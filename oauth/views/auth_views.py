from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from oauth import serializers
from oauth.services import google


def google_login(request):
    return render(request, 'google_login.html')


@api_view(["POST"])
def google_auth(request):
    google_data = serializers.GoogleAuth(data=request.data)
    if google_data.is_valid():
        token = google.check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
