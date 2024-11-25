# Generated by Django 5.0.1 on 2024-11-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifierInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.CharField(max_length=30)),
                ('classifier_model', models.CharField(max_length=30)),
                ('classifier_scaler', models.CharField(max_length=30)),
                ('accuracy', models.CharField(max_length=30)),
                ('f1score', models.CharField(max_length=30)),
                ('precision', models.CharField(max_length=30)),
                ('recall', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CsvUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='', verbose_name='Upload a CSV file')),
            ],
        ),
    ]