# Generated by Django 5.0.6 on 2024-06-06 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0008_user_user_type'),
        ('studentLife_system', '0011_jobfair_applicationdeadline_jobfair_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_student', to='studentLife_system.studentinfo'),
        ),
    ]