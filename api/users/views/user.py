from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

from ..models.user import User, UserSerializer,UserUpdateSerializer

class UserView(APIView):
    def get(self, user_id):
        content = {
            "status": 0
        }

        try:
            user = User.objects.get(user_id=user_id)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_data = UserSerializer(user).data
        content['status']=1
        content[user_data] = user_data
        return JsonResponse(content, status=status.HTTP_201_CREATED)

    def post(self, user_id):
        pass

    def update(self, request, user_id):
        content={}
        user_instance = User.objects.get(user_id=user_id)
        data = UserUpdateSerializer(instance=user_instance, data=request.data)

        if data.is_valid():
            data.save()
            content['massage'] = 'updated successfully'
            return JsonResponse(content, status=status.HTTP_200_OK)
        else:
            content['massage'] = 'failed'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)

    def delete(self, user_id):
        content={}
        try:
            user_instance = User.objects.get(user_id=user_id)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_instance.delete()
        content['massage']='Deleted successfully'
        return JsonResponse(content, status=status.HTTP_200_OK)