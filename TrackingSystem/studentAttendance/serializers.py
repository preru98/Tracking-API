from rest_framework import serializers
from studentAttendance.models import Tag,Student,Admin,TapTiming
from django.utils import timezone

class StudentSerializer(serializers.Serializer):
    enrollmentNumber=serializers.CharField(max_length=20)
    name=serializers.CharField(max_length=2000)
    course=serializers.CharField(max_length=2000)
    year=serializers.CharField(max_length=2000)
    password=serializers.CharField(max_length=2000)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        


class AdminSerializer(serializers.Serializer):
    adminID=serializers.CharField(max_length=2000)
    password=serializers.CharField(max_length=2000)

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)



class TagSerializer(serializers.Serializer):
    tagUID=serializers.CharField(max_length=200)
    #student=serializers.OneToOneField(Student,on_delete=models.CASCADE)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)



class TapTimingSerializer(serializers.Serializer):
    tapAt=serializers.DateTimeField(default=timezone.now)
    #tag=serializers.ForeignKey(Tag, on_delete=models.CASCADE)

    def create(self, validated_data):
        return TapTiming.objects.create(**validated_data)
