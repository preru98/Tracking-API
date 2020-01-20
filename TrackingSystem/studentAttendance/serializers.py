from rest_framework import serializers
from studentAttendance.models import Tag,Student,Admin,TapTiming
from django.utils import timezone


class StudentSerializer(serializers.Serializer):
    enrollmentNumber=serializers.CharField(max_length=20)
    name=serializers.CharField(max_length=2000)
    course=serializers.CharField(max_length=2000)
    year=serializers.CharField(max_length=2000)
    password=serializers.CharField(max_length=2000)

    def create(self, validated_data):        #create : +create()+ save()  
        #print(**validated_data)
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.enrollmentNumber = validated_data.get('enrollmentNumber', instance.enrollmentNumber)
        instance.name = validated_data.get('name', instance.name)
        instance.course = validated_data.get('course', instance.course)
        instance.year = validated_data.get('year', instance.year)
        instance.password = validated_data.get('style', instance.password)
        instance.save()
        return instance
        


class AdminSerializer(serializers.Serializer):
    adminID=serializers.CharField(max_length=2000)
    password=serializers.CharField(max_length=2000)

    def create(self, validated_data):

        return Admin.objects.create(**validated_data)



class TagSerializer(serializers.Serializer):
    tagUID=serializers.CharField(max_length=200)
    student=serializers.CharField(max_length=20,read_only = True)

    def create(self, validated_data):
        enroll=validated_data['student']
        get_student=Student.objects.get(pk=enroll)
        
        new_validated_data={
            'student':get_student, 
            'tagUID' :validated_data['tagUID']
        }
        
        newTag= Tag.objects.create(**new_validated_data)
        # newTag.student=get_student
        newTag.save()
        return newTag

class StudentAndTagRequestSerializer(serializers.Serializer):
    tagUID=serializers.CharField(max_length=200)
    studentEnroll=serializers.CharField(max_length=20)


class TapTimingSerializer(serializers.Serializer):
    tapAt=serializers.DateTimeField(default=timezone.now,format=" %A, %d %B %Y at %H:%M:%S")
    #tag=serializers.CharField(max_length=200,read_only = True)

    def create(self, validated_data):
        return TapTiming.objects.create(**validated_data)
