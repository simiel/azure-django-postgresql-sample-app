# Generated by Django 4.1.7 on 2023-03-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('cv', models.FileField(upload_to='')),
                ('cover_letter', models.FileField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('fulltime', models.BooleanField()),
                ('level', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('deadline', models.DateField()),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
