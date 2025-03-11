from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models.Instructors import Instructor, InstructorSerializer,InstructorUpdateSerializer

class InstructorView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request, instructor_id):
        content = {
            "status": 0
        }

        try:
            user = Instructor.objects.get(Instructor_id=instructor_id)
            print(user)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_data = InstructorSerializer(user).data
        content['status']=1
        content['user_data'] = user_data
        return JsonResponse(content, status=status.HTTP_200_OK)

    def post(self,request, instructor_id):
        pass

    def patch(self, request, instructor_id):
        content={}
        try:
            user_instance = Instructor.objects.get(Instructor_id=instructor_id)
        except:
            content['massage'] = 'failed'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        data = InstructorUpdateSerializer(instance=user_instance, data=request.data, partial=True)

        if data.is_valid():
            data.save()
            content['massage'] = 'updated successfully'
            content['status'] = 1
            content['user_data']=data.data
            return JsonResponse(content, status=status.HTTP_200_OK)
        else:
            content['massage'] = 'failed'
            return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, instructor_id):
        content={}
        try:
            user_instance = Instructor.objects.get(Instructor_id=instructor_id)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_instance.delete()
        content['massage']='Deleted successfully'
        return JsonResponse(content, status=status.HTTP_200_OK)