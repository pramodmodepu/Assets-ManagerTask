# Generated by Django 3.0 on 2021-02-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210204_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='specifications',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]