# Generated by Django 4.2.1 on 2023-06-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employee_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=20),
            preserve_default=False,
        ),
    ]
