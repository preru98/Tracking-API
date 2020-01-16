from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from studentAttendance.models import Tag,Student,Admin,TapTiming
from studentAttendance.serializers import TagSerializer,StudentSerializer,AdminSerializer,TapTimingSerializer

# Create your views here.

#List of Registered Students
def student_list(request):
    if request.method == 'GET':
        allStudents = Student.objects.all()
        serializer = StudentSerializer(allStudents, many=True)
        return JsonResponse(serializer.data, safe=False)



#Detail of a Student
def student_detail(request,enroll):
    if request.method == 'GET':
        try:
            student=Student.objects.get(pk=enroll)
        except Student.DoesNotExist:
            return HttpResponse(status=404)

        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)


#Register Student       
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_delete(request,enroll):
    print (request.method)
    try:
        student=Student.objects.get(pk=enroll)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':       #We are using POST, instead. Just end with trailing slash and does not include body
        student.delete()
        return HttpResponse(status=204)

@csrf_exempt
def student_update(request,enroll):
    try:
        student=Student.objects.get(pk=enroll)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':                 #end url with trailing slash : http://localhost:8000/update/6/
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def tag_create(request):
   
    if request.method == 'POST':
        data = JSONParser().parse(request)
        enroll=data['student']
        try:
            student=Student.objects.get(pk=enroll)
        except Student.DoesNotExist:
            return HttpResponse(status=404)

        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def map_tag(request):

    if request.method=='POST':
        data=JSONParser().parse(request)
        enroll=data['studentRollNumber']
        student=Student.objects.get(pk=enroll)
        tagId=data['tag']
        newTag=Tag(tagUID=tagId,student=student)
        newTag.save()
        responseDict={
            'successful':True,

            }
        tagObject=JSONParser().parse(newTag)
        return JsonResponse(tagObject,status=200)

@csrf_exempt
def map_tag(request):

    if request.method=='POST':
        data=JSONParser().parse(request)
        enroll=data['studentRollNumber']
        student=Student.objects.get(pk=enroll)
        tagId=data['tag']
        newTag=Tag(tagUID=tagId,student=student)
        newTag.save()
        responseDict={
            'successful':True,
        }
        # tagObject=JSONParser().parse(newTag)
        return JsonResponse(responseDict,status=200)

def tag_list(request):
    if request.method == 'GET':
        allTags = Tag.objects.all()
        serializer = TagSerializer(allTags, many=True)
        return JsonResponse(serializer.data, safe=False)


#Todo Register as alumni
#Users:
    #Student : view all details
    #Admin   : CRUD on student
    #Teachers: View academic details only
    #Register time ,see date time in documen.

