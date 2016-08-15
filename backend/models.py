from __future__ import unicode_literals
from django.db import models
# Create your models here.
GENDER_CHOICES=(('M','Male'),('F','Female'),)
class Patient(models.Model):
    idnum = models.CharField(max_length=18,unique=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    #use p.get_gender_display() to display Male or Female else then display M or F
    age = models.IntegerField()
    owner = models.ForeignKey('auth.User',related_name = 'patient')

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True)
    patient = models.ManyToManyField(Patient,through='DateAndValue')

    def __unicode__(self):
        return self.name

class DateAndValue(models.Model):
    patient = models.ForeignKey(Patient)
    project = models.ForeignKey(Project)
    date_tested = models.DateTimeField(auto_now=True)
    value_tested = models.IntegerField()
    owner = models.ForeignKey('auth.User',related_name = 'test')

    def __unicode__(self):
        return '%s got %d point in the %s at %s'%(self.patient.name,self.value_tested,self.project.name,self.date_tested)
