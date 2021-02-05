# Generated by Django 3.0 on 2021-02-03 05:21

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('is_employee_master', models.BooleanField(default=False)),
                ('is_asset_master', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop', models.CharField(max_length=150)),
                ('modems', models.CharField(max_length=50)),
                ('tools', models.CharField(max_length=50)),
                ('operating_system', models.CharField(max_length=50)),
                ('is_alloted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStockKeyMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField()),
                ('issue', models.CharField(max_length=200)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Stock')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]
