# Generated by Django 4.1.7 on 2023-03-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_alter_attendance_date_alter_course_start_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="token_id",
            field=models.CharField(default="97735001", max_length=150),
        ),
    ]
