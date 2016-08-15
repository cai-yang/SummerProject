# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateAndValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_tested', models.DateTimeField(auto_now=True)),
                ('value_tested', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(max_length=18, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('patient', models.ManyToManyField(through='backend.DateAndValue', to='backend.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='dateandvalue',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Patient'),
        ),
        migrations.AddField(
            model_name='dateandvalue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Project'),
        ),
    ]