# Generated by Django 5.0.6 on 2024-06-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentLife_system', '0018_remove_studentinfo_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exceldata',
            name='admin_remarks',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='exceldata',
            name='variance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
