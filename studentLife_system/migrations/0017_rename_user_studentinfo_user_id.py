# Generated by Django 5.0.6 on 2024-06-06 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentLife_system', '0016_studentinfo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='user',
            new_name='user_id',
        ),
    ]
