# Generated by Django 5.0.4 on 2024-06-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sanction_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]