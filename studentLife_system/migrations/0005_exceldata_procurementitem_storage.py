# Generated by Django 5.0.6 on 2024-06-02 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentLife_system', '0004_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_l_d', models.CharField(max_length=255, verbose_name='Title of L & D')),
                ('frequency', models.CharField(max_length=255, verbose_name='Frequency (Annual, Semi-Annual, Quarterly)')),
                ('category', models.CharField(max_length=255, verbose_name='Category (International, National & Regional/Local)')),
                ('expected_number_of_participants', models.CharField(max_length=255, verbose_name='Expected Number of Participants')),
                ('duration', models.CharField(max_length=255, verbose_name='Duration')),
                ('registration_fees', models.CharField(max_length=255, verbose_name='Registration Fees')),
                ('travelling_expenses', models.CharField(max_length=255, verbose_name='Travelling Expenses (Per Diem and Transportation)')),
                ('planned_total_budget', models.CharField(max_length=255, verbose_name='Planned Total Budget')),
                ('actual_total_budget', models.CharField(max_length=255, verbose_name='Actual Total Budget')),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementItem',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unit', models.CharField(default='your_default_value', max_length=50)),
                ('estimated_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode_of_procurement', models.CharField(max_length=255)),
                ('jan', models.IntegerField(default=0)),
                ('feb', models.IntegerField(default=0)),
                ('mar', models.IntegerField(default=0)),
                ('apr', models.IntegerField(default=0)),
                ('may', models.IntegerField(default=0)),
                ('jun', models.IntegerField(default=0)),
                ('jul', models.IntegerField(default=0)),
                ('aug', models.IntegerField(default=0)),
                ('sep', models.IntegerField(default=0)),
                ('oct', models.IntegerField(default=0)),
                ('nov', models.IntegerField(default=0)),
                ('dec', models.IntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('for_purchase', 'For Purchase'), ('purchased', 'Purchased'), ('delivered', 'Delivered')], default='for_purchase', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('procurement_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studentLife_system.procurementitem')),
            ],
        ),
    ]
