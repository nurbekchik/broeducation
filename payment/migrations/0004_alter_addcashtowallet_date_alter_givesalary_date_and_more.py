# Generated by Django 4.1.7 on 2023-03-08 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_alter_addcashtowallet_date_alter_givesalary_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addcashtowallet",
            name="date",
            field=models.DateField(default=datetime.date(2023, 3, 8)),
        ),
        migrations.AlterField(
            model_name="givesalary",
            name="date",
            field=models.DateField(default=datetime.date(2023, 3, 8)),
        ),
        migrations.AlterField(
            model_name="paytocourse",
            name="date",
            field=models.DateField(default=datetime.date(2023, 3, 8)),
        ),
    ]
