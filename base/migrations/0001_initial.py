# Generated by Django 5.0.4 on 2024-06-06 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('received_by', models.CharField(max_length=100)),
                ('reported_by', models.CharField(max_length=100)),
                ('case_date', models.DateField()),
                ('case_class', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('lrn', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('degree', models.CharField(max_length=100)),
                ('year_level', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
                ('sanction', models.CharField(blank=True, choices=[('apology_letter', 'Apology Letter'), ('community_service', 'Community Service'), ('suspension', 'Suspension'), ('expulsion', 'Expulsion')], max_length=50, null=True)),
                ('sanction_completed', models.BooleanField(default=False)),
                ('apology_letter', models.FileField(blank=True, null=True, upload_to='apology_letters/')),
                ('community_service_hours', models.IntegerField(blank=True, null=True)),
                ('community_service_deadline', models.DateField(blank=True, null=True)),
                ('suspension_start_date', models.DateField(blank=True, null=True)),
                ('suspension_end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course_year_section', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodMoral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('case_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.caseprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityServiceTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('time_in', models.IntegerField()),
                ('time_out', models.IntegerField()),
                ('time_rendered', models.IntegerField()),
                ('student_signature', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
        ),
        migrations.AddField(
            model_name='caseprofile',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student'),
        ),
    ]