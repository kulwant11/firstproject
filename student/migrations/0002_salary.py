# Generated by Django 4.0 on 2021-12-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_salary', models.IntegerField()),
                ('emp_name', models.CharField(max_length=30)),
            ],
        ),
    ]