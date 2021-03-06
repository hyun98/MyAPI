from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from knox.models import AuthToken
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from accountapp.serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if(len(request.data['username']) < 6 or len(request.data['password']) < 4):
            body = {'message': "too short"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': AuthToken.objects.create(user)[1],
            }
        )

    # def get(self, request):
    #     return render(request, 'account/register.html')


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        # data = {
        #     'close': 'close_list',
        #     'open': 'open_list',
        #     'high': 'high_list',
        #     'low': 'low_list',
        #     'vol': 'vol_list',
        # }
        # return JsonResponse(data)
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': AuthToken.objects.create(user)[1],
            }
        )

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


def ShowUser(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'hello.html', context)


def AccountIDCheck(request):
    if (request.method == 'POST'):
        username = request.POST['username']
    else:
        username = ''
    user = User
    idObject = user.objects.filter(username__exact=username)
    idCount = idObject.count()

    if idCount > 0:
        msg = "<span>?????? ???????????? ID?????????.</span><input type='hidden' name='idcheck-result'\
               id='IDCheckResult' value=0>"
    else:
        msg = "<span>????????? ??? ?????? ID?????????.</span><input type='hidden' name='idcheck-result'\
               id='IDCheckResult' value=1>"

    return HttpResponse(msg)
