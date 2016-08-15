from rest_framework import serializers
from backend.models import *
from django.contrib.auth.models import User

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Patient
        fields = ('url','owner','idnum','name','gender','age')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url','name','patient')

class DateAndValueSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = DateAndValue
        fields = ('url','owner','patient','project','date_tested','value_tested')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='patient-detail')
    test = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='dateandvalue-detail')
    class Meta:
        model = User
        fields = ('url','username','patient','test')
