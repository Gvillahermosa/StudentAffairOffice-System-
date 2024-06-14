# Generated by Django 4.2.4 on 2024-06-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentLife_system', '0023_mod_program_projects_qrdonation'),
        ('jobplacement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ojtrequirements',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentLife_system.studentinfo'),
        ),
        migrations.AlterField(
            model_name='ojtstudent',
            name='studID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='studentLife_system.studentinfo'),
        ),
        migrations.AlterField(
            model_name='seminarattendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentLife_system.studentinfo'),
        ),
        migrations.DeleteModel(
            name='StudentUser',
        ),
    ]