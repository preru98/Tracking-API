from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from studentAttendance.models import Tag,Student,Admin,TapTiming
from studentAttendance.serializers import TagSerializer,StudentSerializer,AdminSerializer,TapTimingSerializer

# Create your views here.

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        allStudents = Student.objects.all()
        serializer = StudentSerializer(allStudents, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

